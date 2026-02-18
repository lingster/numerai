#!/usr/bin/env python3
"""Numerai Round Performance Viewer - CLI entry point.

Commands: round, cache, returns, position, growth
"""

import re
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Annotated, Optional

import typer
from loguru import logger

from numerai_client import NumeraiGraphQLClient
from round_cache import build_cache_dataframe, flush_to_parquet, get_cached_rounds, load_parquet, read_cache_for_round, read_round_from_df, save_to_parquet
from round_config import DEFAULT_CONFIG_PATH, AppConfig, load_config
from round_display import apply_overrides, display_results, display_timing
from round_fetchers import fetch_latest_round, fetch_permodel, fetch_rounddetails, fetch_rounddetails_raw
from round_position import compute_positions, get_metric_label, plot_positions
from round_returns import calculate_cumulative, display_detail, display_summary, gather_returns, resolve_round_range

logger.remove()

app = typer.Typer(help="Numerai round model performance viewer")


def _setup_logging(verbose: bool) -> None:
    level = "DEBUG" if verbose else "INFO"
    logger.add(sys.stderr, level=level, format="{time:HH:mm:ss} | {level:<7} | {message}")


@app.command()
def round(
    round_number: Annotated[int, typer.Argument(help="Round number to query")],
    model_regex: Annotated[str, typer.Argument(help="Regex pattern for model names")] = ".*",
    tournament: Annotated[Optional[str], typer.Option("-t", "--tournament", help="classic|signals|crypto (or 8/11/12)")] = None,
    mmc_mult: Annotated[Optional[float], typer.Option("--mmc-mult", help="MMC multiplier")] = None,
    corr_mult: Annotated[Optional[float], typer.Option("--corr-mult", help="CORR multiplier")] = None,
    method: Annotated[Optional[str], typer.Option("-m", "--method", help="rounddetails|permodel|both")] = None,
    both: Annotated[bool, typer.Option("--both", "-b", help="Run both methods and compare timing")] = False,
    sort_by: Annotated[Optional[str], typer.Option("-s", "--sort", help="return_pct|mmc20|corr20|model_name")] = None,
    descending: Annotated[Optional[bool], typer.Option("--desc/--asc", help="Sort direction")] = None,
    max_models: Annotated[Optional[int], typer.Option("--max-models", help="Max models for permodel method")] = None,
    from_cache: Annotated[bool, typer.Option("--from-cache", help="Read from parquet cache instead of live API")] = False,
    parquet_path: Annotated[Optional[Path], typer.Option("--parquet-path", help="Path to parquet cache file")] = None,
    config_path: Annotated[Path, typer.Option("-c", "--config", help="Config YAML path")] = DEFAULT_CONFIG_PATH,
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Enable debug logging")] = False,
):
    """
    Query and display model performance for a specific Numerai round.

    Examples:
        uv run round_performance.py round 1182 "nasdaqjockey.*"
        uv run round_performance.py round 1182 ".*" -t signals
        uv run round_performance.py round 1182 "fnc_imp" --both
        uv run round_performance.py round 1182 "nasdaqjockey.*" --from-cache
    """
    _setup_logging(verbose)

    cfg = load_config(config_path)
    apply_overrides(
        cfg, tournament=tournament, mmc_mult=mmc_mult, corr_mult=corr_mult,
        method=method, both=both, sort_by=sort_by, descending=descending,
        max_models=max_models, parquet_path=parquet_path,
    )
    if model_regex != ".*" or cfg.model_regex is None:
        cfg.model_regex = model_regex

    try:
        pattern = re.compile(cfg.model_regex or ".*", re.IGNORECASE)
    except re.error as e:
        logger.error(f"Invalid regex '{cfg.model_regex}': {e}")
        raise typer.Exit(1)

    formula = cfg.get_formula()
    col_headers = formula.column_headers
    logger.info(f"Round {round_number} | regex='{pattern.pattern}' | tournament={cfg.tournament.name.lower()}")
    logger.info(f"Formula: {formula.description}")

    if from_cache:
        cache_path = cfg.get_parquet_path()
        t = time.perf_counter()
        results = read_cache_for_round(cache_path, round_number, pattern, formula)
        t = time.perf_counter() - t
        display_results(results, f"Round {round_number} - cache ({t:.3f}s)", cfg.sort_by, cfg.sort_desc, col_headers)
        return

    with NumeraiGraphQLClient() as client:
        if cfg.method == "both":
            t1 = time.perf_counter()
            r1 = fetch_rounddetails(client, cfg.tournament, round_number, pattern, formula)
            t1 = time.perf_counter() - t1
            t2 = time.perf_counter()
            r2 = fetch_permodel(client, cfg.tournament, round_number, pattern, formula, cfg.max_models)
            t2 = time.perf_counter() - t2
            display_results(r1, f"Round {round_number} - rounddetails ({t1:.3f}s)", cfg.sort_by, cfg.sort_desc, col_headers)
            display_results(r2, f"Round {round_number} - permodel ({t2:.3f}s)", cfg.sort_by, cfg.sort_desc, col_headers)
            display_timing(t1, t2, len(r1), len(r2))
        elif cfg.method == "permodel":
            t = time.perf_counter()
            results = fetch_permodel(client, cfg.tournament, round_number, pattern, formula, cfg.max_models)
            t = time.perf_counter() - t
            display_results(results, f"Round {round_number} - permodel ({t:.3f}s)", cfg.sort_by, cfg.sort_desc, col_headers)
        else:
            t = time.perf_counter()
            results = fetch_rounddetails(client, cfg.tournament, round_number, pattern, formula)
            t = time.perf_counter() - t
            display_results(results, f"Round {round_number} - rounddetails ({t:.3f}s)", cfg.sort_by, cfg.sort_desc, col_headers)


@app.command()
def cache(
    start_round: Annotated[int, typer.Argument(help="First round to cache")],
    end_round: Annotated[Optional[int], typer.Argument(help="Last round to cache (default: latest)")] = None,
    update: Annotated[bool, typer.Option("--update", help="Re-fetch rounds already in cache")] = False,
    tournament: Annotated[Optional[str], typer.Option("-t", "--tournament", help="classic|signals|crypto (or 8/11/12)")] = None,
    batch_size: Annotated[int, typer.Option("--batch-size", help="Rounds per batch write")] = 20,
    parquet_path: Annotated[Optional[Path], typer.Option("--parquet-path", help="Path to parquet cache file")] = None,
    config_path: Annotated[Path, typer.Option("-c", "--config", help="Config YAML path")] = DEFAULT_CONFIG_PATH,
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Enable debug logging")] = False,
):
    """
    Download round details to a local parquet file for offline lookups.
    Fetches rounds concurrently and writes in batches for speed.

    Examples:
        uv run round_performance.py cache 1180 1182
        uv run round_performance.py cache 1180 -t signals
        uv run round_performance.py cache 200 220 -t 8 --batch-size 5
    """
    _setup_logging(verbose)

    cfg = load_config(config_path)
    apply_overrides(cfg, tournament=tournament, parquet_path=parquet_path)
    cache_path = cfg.get_parquet_path()

    with NumeraiGraphQLClient() as client:
        if end_round is None:
            end_round = fetch_latest_round(client, cfg.tournament)
            logger.info(f"Latest round: {end_round}")

        if start_round > end_round:
            logger.error(f"start_round ({start_round}) > end_round ({end_round})")
            raise typer.Exit(1)

        all_rounds = list(range(start_round, end_round + 1))
        cached = get_cached_rounds(cache_path)
        rounds_to_fetch = all_rounds if update else [r for r in all_rounds if r not in cached]

        skipped = len(all_rounds) - len(rounds_to_fetch)
        if not rounds_to_fetch:
            typer.echo(f"All {len(all_rounds)} rounds already cached. Use --update to re-fetch.")
            return

        logger.info(
            f"Fetching {len(rounds_to_fetch)} rounds ({skipped} skipped) "
            f"for tournament {cfg.tournament.name.lower()} | batch_size={batch_size}"
        )

        _cache_parallel(client, cfg, cache_path, rounds_to_fetch, cached, update, batch_size, skipped)


def _fetch_round(
    client: NumeraiGraphQLClient,
    tournament: int,
    round_number: int,
) -> tuple[int, "pl.DataFrame | None"]:
    """Worker: fetch a single round and return (round_number, df_or_None)."""
    import polars as pl

    pf, raw_models = fetch_rounddetails_raw(client, tournament, round_number)
    if not raw_models:
        logger.warning(f"Round {round_number}: no models returned, skipping")
        return round_number, None
    df = build_cache_dataframe(round_number, tournament, pf, raw_models)
    return round_number, df


def _cache_parallel(
    client: NumeraiGraphQLClient,
    cfg: AppConfig,
    cache_path: Path,
    rounds_to_fetch: list[int],
    cached: set[int],
    update: bool,
    batch_size: int,
    skipped: int,
) -> None:
    """Fetch rounds concurrently, flush to parquet in batches, handle Ctrl+C."""
    import polars as pl

    interrupted = False
    original_sigint = signal.getsignal(signal.SIGINT)

    def _on_sigint(signum, frame):
        nonlocal interrupted
        interrupted = True
        typer.echo("\nInterrupt received. Finishing in-flight requests...")

    signal.signal(signal.SIGINT, _on_sigint)

    existing_df = load_parquet(cache_path)
    buffer: list[pl.DataFrame] = []
    rounds_to_replace: set[int] = set()
    saved = 0
    total = len(rounds_to_fetch)
    t_start = time.perf_counter()

    try:
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = {}
            for i, rnd in enumerate(rounds_to_fetch):
                if interrupted:
                    break
                future = pool.submit(_fetch_round, client, cfg.tournament, rnd)
                futures[future] = rnd
                # Rate-limit submissions: 1s delay between each
                if i < len(rounds_to_fetch) - 1 and not interrupted:
                    time.sleep(1)

            for future in as_completed(futures):
                rnd, df = future.result()
                if df is not None:
                    buffer.append(df)
                    if update and rnd in cached:
                        rounds_to_replace.add(rnd)
                    saved += 1
                    typer.echo(f"Fetched round {rnd} ({saved}/{total})")

                # Flush when buffer is full
                if len(buffer) >= batch_size:
                    existing_df = flush_to_parquet(existing_df, buffer, cache_path, rounds_to_replace)
                    buffer.clear()
                    rounds_to_replace.clear()

                if interrupted:
                    # Cancel pending futures
                    for f in futures:
                        f.cancel()
                    break
    finally:
        # Always flush remaining buffer
        if buffer:
            msg = f"Saving {len(buffer)} buffered rounds..." if interrupted else f"Final flush: {len(buffer)} rounds"
            typer.echo(msg)
            existing_df = flush_to_parquet(existing_df, buffer, cache_path, rounds_to_replace)

        signal.signal(signal.SIGINT, original_sigint)

    elapsed = time.perf_counter() - t_start
    total_rows = len(existing_df) if not existing_df.is_empty() else 0
    typer.echo(f"Cached {saved} rounds ({skipped} skipped) in {elapsed:.1f}s. Total rows in {cache_path}: {total_rows}")


@app.command()
def returns(
    start_round: Annotated[int, typer.Argument(help="First round number")],
    model_regex: Annotated[str, typer.Argument(help="Regex pattern for model names")] = ".*",
    end_round: Annotated[Optional[int], typer.Option("-e", "--end-round", help="Last round (default: latest cached or latest API round)")] = None,
    tournament: Annotated[Optional[str], typer.Option("-t", "--tournament", help="classic|signals|crypto (or 8/11/12)")] = None,
    live: Annotated[bool, typer.Option("--live", help="Fetch from live API instead of cache")] = False,
    summary: Annotated[bool, typer.Option("--summary", help="Show only summary table (no per-round detail)")] = False,
    parquet_path: Annotated[Optional[Path], typer.Option("--parquet-path", help="Path to parquet cache file")] = None,
    config_path: Annotated[Path, typer.Option("-c", "--config", help="Config YAML path")] = DEFAULT_CONFIG_PATH,
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Enable debug logging")] = False,
):
    """
    Calculate cumulative returns across multiple rounds.

    Reads from parquet cache by default. Use --live to query the API.
    Shows per-round detail for a single model, summary table for multiple.
    Use --summary to always show the summary table.

    Examples:
        uv run round_performance.py returns 1170 "^fnc_imp"
        uv run round_performance.py returns 1170 "^fnc" --summary
        uv run round_performance.py returns 1170 "^fnc" -t crypto --live
        uv run round_performance.py returns 1170 "^fnc" -e 1180
    """
    _setup_logging(verbose)

    cfg = load_config(config_path)
    apply_overrides(cfg, tournament=tournament, parquet_path=parquet_path)

    try:
        pattern = re.compile(model_regex, re.IGNORECASE)
    except re.error as e:
        logger.error(f"Invalid regex '{model_regex}': {e}")
        raise typer.Exit(1)

    formula = cfg.get_formula()
    logger.info(f"Tournament: {cfg.tournament.name.lower()} | Formula: {formula.description}")

    client = None
    try:
        if live:
            client = NumeraiGraphQLClient()
            client.__enter__()

        rounds = resolve_round_range(start_round, end_round, cfg, live, client)
        logger.info(f"Rounds {rounds[0]}-{rounds[-1]} ({len(rounds)} rounds) | regex='{pattern.pattern}'")

        t = time.perf_counter()
        model_rounds = gather_returns(rounds, pattern, formula, cfg, live, client)
        cumulative = calculate_cumulative(model_rounds, len(rounds))
        t = time.perf_counter() - t

        title = f"Cumulative Returns: rounds {rounds[0]}-{rounds[-1]} ({cfg.tournament.name.lower()}, {t:.3f}s)"

        if not cumulative:
            typer.echo("No matching models found.")
            return

        if len(cumulative) == 1 and not summary:
            display_detail(cumulative[0], title, formula.column_headers)
        else:
            display_summary(cumulative, title, cfg.sort_desc)
    finally:
        if client is not None:
            client.__exit__(None, None, None)


@app.command()
def position(
    start_round: Annotated[int, typer.Argument(help="First round number")],
    model_regex: Annotated[str, typer.Argument(help="Regex pattern for model names")] = ".*",
    end_round: Annotated[Optional[int], typer.Option("-e", "--end-round", help="Last round (default: latest cached)")] = None,
    tournament: Annotated[Optional[str], typer.Option("-t", "--tournament", help="classic|signals|crypto (or 8/11/12)")] = None,
    metric: Annotated[Optional[str], typer.Option("--metric", help="return_pct|score1|score2")] = None,
    width: Annotated[int, typer.Option("-w", "--width", help="Plot width in columns")] = 120,
    height: Annotated[int, typer.Option("-h", "--height", help="Plot height in rows")] = 30,
    parquet_path: Annotated[Optional[Path], typer.Option("--parquet-path", help="Path to parquet cache file")] = None,
    config_path: Annotated[Path, typer.Option("-c", "--config", help="Config YAML path")] = DEFAULT_CONFIG_PATH,
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Enable debug logging")] = False,
):
    """
    Plot model rank/percentile position across rounds from the parquet cache.

    Shows how a model's relative standing changes over time. Lower percentile = better.

    Examples:
        uv run round_performance.py position 1170 "nasdaqjockey.*"
        uv run round_performance.py position 1170 "^fnc_imp" --metric score1
        uv run round_performance.py position 1170 "^fnc_imp" -t crypto
    """
    _setup_logging(verbose)

    cfg = load_config(config_path)
    apply_overrides(cfg, tournament=tournament, parquet_path=parquet_path)
    if metric is not None:
        cfg.position_metric = metric

    try:
        pattern = re.compile(model_regex, re.IGNORECASE)
    except re.error as e:
        logger.error(f"Invalid regex '{model_regex}': {e}")
        raise typer.Exit(1)

    formula = cfg.get_formula()
    cache_path = cfg.get_parquet_path()

    cached = get_cached_rounds(cache_path)
    if not cached:
        typer.echo(f"No cached rounds in {cache_path}. Run 'cache' first.")
        raise typer.Exit(1)

    if end_round is None:
        end_round = max(cached)
    rounds = list(range(start_round, end_round + 1))

    metric_label = get_metric_label(formula, cfg.position_metric)
    logger.info(
        f"Position: rounds {start_round}-{end_round} | metric={metric_label} "
        f"| tournament={cfg.tournament.name.lower()} | regex='{pattern.pattern}'"
    )

    df = compute_positions(cache_path, rounds, pattern, formula, cfg.position_metric)
    if df.is_empty():
        typer.echo("No matching models found.")
        raise typer.Exit(1)

    title = f"Position by {metric_label}: rounds {start_round}-{end_round} ({cfg.tournament.name.lower()})"
    plot_positions(df, title, width, height)


TOURNAMENT_COLORS: dict[str, str] = {
    "classic": "blue",
    "signals": "green",
    "crypto": "orange",
}


@app.command()
def growth(
    tournament: Annotated[Optional[str], typer.Option("-t", "--tournament", help="classic|signals|crypto (or 8/11/12)")] = None,
    pf: Annotated[bool, typer.Option("--pf", help="Plot payout factor instead of model count")] = False,
    count: Annotated[bool, typer.Option("--count", help="Plot model count (combine with --pf for dual-axis chart)")] = False,
    width: Annotated[int, typer.Option("-w", "--width", help="Plot width in columns")] = 120,
    height: Annotated[int, typer.Option("-h", "--height", help="Plot height in rows")] = 30,
    parquet_path: Annotated[Optional[Path], typer.Option("--parquet-path", help="Path to parquet cache file")] = None,
    config_path: Annotated[Path, typer.Option("-c", "--config", help="Config YAML path")] = DEFAULT_CONFIG_PATH,
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Enable debug logging")] = False,
):
    """
    Plot the growth in total model count per round from the parquet cache.
    Use --pf to plot payout factor. Without -t, --pf overlays all tournaments.
    Use --pf --count for a dual-axis chart with both metrics.

    Examples:
        uv run round_performance.py growth
        uv run round_performance.py growth -t crypto
        uv run round_performance.py growth --pf
        uv run round_performance.py growth --pf --count
        uv run round_performance.py growth --pf --count -t classic
        uv run round_performance.py growth -w 80 -h 20
    """
    _setup_logging(verbose)

    import plotext as plt
    from round_cache import load_parquet

    cfg = load_config(config_path)
    apply_overrides(cfg, tournament=tournament, parquet_path=parquet_path)

    if pf and count:
        if tournament is None:
            _plot_both_all_tournaments(cfg, plt, load_parquet, width, height)
        else:
            _plot_both_single(cfg, plt, load_parquet, width, height)
    elif pf and tournament is None:
        _plot_pf_all_tournaments(cfg, plt, load_parquet, width, height)
    elif pf:
        _plot_pf_single(cfg, plt, load_parquet, width, height)
    elif tournament is None:
        _plot_model_count_all_tournaments(cfg, plt, load_parquet, width, height)
    else:
        _plot_model_count(cfg, plt, load_parquet, width, height)


def _plot_model_count(cfg, plt, load_parquet, width: int, height: int) -> None:
    """Plot model count growth for a single tournament."""
    import polars as pl

    cache_path = cfg.get_parquet_path()
    df = load_parquet(cache_path)
    if df.is_empty() or "round_number" not in df.columns:
        typer.echo(f"No data in cache {cache_path}. Run 'cache' first.")
        raise typer.Exit(1)

    counts = df.group_by("round_number").len().sort("round_number")
    rounds = counts["round_number"].to_list()
    model_counts = counts["len"].to_list()

    logger.info(f"Rounds {rounds[0]}-{rounds[-1]}: {len(rounds)} data points")

    tournament_name = cfg.tournament.name.lower()
    plt.clear_figure()
    plt.plot_size(width, height)
    plt.plot(rounds, model_counts, marker="braille")
    plt.title(f"Model Count Growth ({tournament_name})")
    plt.xlabel("Round Number")
    plt.ylabel("Total Models")
    plt.show()


def _plot_model_count_all_tournaments(cfg, plt, load_parquet, width: int, height: int) -> None:
    """Overlay model count growth for all tournaments that have cached data."""
    from numerai_client import Tournament

    plotted = 0
    plt.clear_figure()
    plt.plot_size(width, height)

    for t in Tournament:
        cfg.tournament = t
        cache_path = cfg.get_parquet_path()
        df = load_parquet(cache_path)
        if df.is_empty() or "round_number" not in df.columns:
            continue

        counts = df.group_by("round_number").len().sort("round_number")
        rounds = counts["round_number"].to_list()
        model_counts = counts["len"].to_list()
        name = t.name.lower()
        color = TOURNAMENT_COLORS.get(name, "white")

        logger.info(f"{name}: rounds {rounds[0]}-{rounds[-1]} ({len(rounds)} points)")
        plt.plot(rounds, model_counts, marker="braille", color=color, label=name)
        plotted += 1

    if plotted == 0:
        typer.echo("No cached data found for any tournament. Run 'cache' first.")
        raise typer.Exit(1)

    plt.title("Model Count Growth (all tournaments)")
    plt.xlabel("Round Number")
    plt.ylabel("Total Models")
    plt.show()


def _plot_pf_single(cfg, plt, load_parquet, width: int, height: int) -> None:
    """Plot payout factor for a single tournament."""
    import polars as pl

    cache_path = cfg.get_parquet_path()
    df = load_parquet(cache_path)
    if df.is_empty() or "round_number" not in df.columns or "payout_factor" not in df.columns:
        typer.echo(f"No data in cache {cache_path}. Run 'cache' first.")
        raise typer.Exit(1)

    pf_df = df.group_by("round_number").agg(pl.col("payout_factor").first()).sort("round_number")
    rounds = pf_df["round_number"].to_list()
    pf_values = pf_df["payout_factor"].to_list()

    tournament_name = cfg.tournament.name.lower()
    color = TOURNAMENT_COLORS.get(tournament_name, "white")
    logger.info(f"Payout factor: rounds {rounds[0]}-{rounds[-1]} ({len(rounds)} points)")

    plt.clear_figure()
    plt.plot_size(width, height)
    plt.plot(rounds, pf_values, marker="braille", color=color, label=tournament_name)
    plt.title(f"Payout Factor ({tournament_name})")
    plt.xlabel("Round Number")
    plt.ylabel("Payout Factor")
    plt.show()


def _plot_pf_all_tournaments(cfg, plt, load_parquet, width: int, height: int) -> None:
    """Overlay payout factor for all tournaments that have cached data."""
    import polars as pl

    from numerai_client import Tournament

    plotted = 0
    plt.clear_figure()
    plt.plot_size(width, height)

    for t in Tournament:
        cfg.tournament = t
        cache_path = cfg.get_parquet_path()
        df = load_parquet(cache_path)
        if df.is_empty() or "payout_factor" not in df.columns:
            continue

        pf_df = df.group_by("round_number").agg(pl.col("payout_factor").first()).sort("round_number")
        rounds = pf_df["round_number"].to_list()
        pf_values = pf_df["payout_factor"].to_list()
        name = t.name.lower()
        color = TOURNAMENT_COLORS.get(name, "white")

        logger.info(f"{name}: rounds {rounds[0]}-{rounds[-1]} ({len(rounds)} points)")
        plt.plot(rounds, pf_values, marker="braille", color=color, label=name)
        plotted += 1

    if plotted == 0:
        typer.echo("No cached data found for any tournament. Run 'cache' first.")
        raise typer.Exit(1)

    plt.title("Payout Factor (all tournaments)")
    plt.xlabel("Round Number")
    plt.ylabel("Payout Factor")
    plt.show()


def _load_count_and_pf(df: "pl.DataFrame") -> tuple["pl.DataFrame", "pl.DataFrame"]:
    """Extract model count and payout factor DataFrames from a dataframe."""
    import polars as pl

    counts = df.group_by("round_number").len().sort("round_number")
    pf_df = df.group_by("round_number").agg(pl.col("payout_factor").first()).sort("round_number")
    return counts, pf_df


def _plot_both_single(cfg, plt, load_parquet, width: int, height: int) -> None:
    """Plot model count (left y-axis) and payout factor (right y-axis) for one tournament."""
    cache_path = cfg.get_parquet_path()
    df = load_parquet(cache_path)
    if df.is_empty() or "round_number" not in df.columns or "payout_factor" not in df.columns:
        typer.echo(f"No data in cache {cache_path}. Run 'cache' first.")
        raise typer.Exit(1)

    tournament_name = cfg.tournament.name.lower()
    color = TOURNAMENT_COLORS.get(tournament_name, "white")
    counts, pf_df = _load_count_and_pf(df)
    rounds = counts["round_number"].to_list()

    logger.info(f"Rounds {rounds[0]}-{rounds[-1]}: {len(counts)} data points")

    plt.clear_figure()
    plt.plot_size(width, height)
    plt.plot(rounds, counts["len"].to_list(), marker="braille", color=color, label=f"{tournament_name} count")
    plt.plot(pf_df["round_number"].to_list(), pf_df["payout_factor"].to_list(), marker="braille", color="red", label=f"{tournament_name} pf", yside="right")
    plt.ylabel("Model Count", yside="left")
    plt.ylabel("Payout Factor", yside="right")
    plt.title(f"Model Count & Payout Factor ({tournament_name})")
    plt.xlabel("Round Number")
    plt.show()


def _plot_both_all_tournaments(cfg, plt, load_parquet, width: int, height: int) -> None:
    """Overlay model count and payout factor for all tournaments on dual y-axes."""
    from numerai_client import Tournament

    plotted = 0
    plt.clear_figure()
    plt.plot_size(width, height)

    for t in Tournament:
        cfg.tournament = t
        cache_path = cfg.get_parquet_path()
        df = load_parquet(cache_path)
        if df.is_empty() or "payout_factor" not in df.columns:
            continue

        name = t.name.lower()
        color = TOURNAMENT_COLORS.get(name, "white")
        counts, pf_df = _load_count_and_pf(df)
        rounds = counts["round_number"].to_list()

        logger.info(f"{name}: rounds {rounds[0]}-{rounds[-1]} ({len(counts)} points)")
        plt.plot(rounds, counts["len"].to_list(), marker="braille", color=color, label=f"{name} count")
        plt.plot(pf_df["round_number"].to_list(), pf_df["payout_factor"].to_list(), marker="dot", color=color, label=f"{name} pf", yside="right")
        plotted += 1

    if plotted == 0:
        typer.echo("No cached data found for any tournament. Run 'cache' first.")
        raise typer.Exit(1)

    plt.ylabel("Model Count", yside="left")
    plt.ylabel("Payout Factor", yside="right")
    plt.title("Model Count & Payout Factor (all tournaments)")
    plt.xlabel("Round Number")
    plt.show()


if __name__ == "__main__":
    app()
