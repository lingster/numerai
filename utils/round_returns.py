"""
Numerai Round Performance - Cumulative Returns Calculator

Calculate cumulative returns across multiple rounds for matched models.
Supports both simple additive and compounded return calculations.
"""

import re
from pathlib import Path
from typing import Optional

import typer
from loguru import logger
from pydantic import BaseModel
from tabulate import tabulate

from numerai_client import NumeraiGraphQLClient
from round_cache import gather_returns_bulk, get_cached_rounds
from round_config import AppConfig, FormulaBase
from round_fetchers import fetch_latest_round, fetch_rounddetails


class RoundReturn(BaseModel):
    """Return data for a single model in a single round."""

    round_number: int
    score1: Optional[float] = None
    score2: Optional[float] = None
    payout_factor: float
    return_pct: Optional[float] = None


class ModelCumulative(BaseModel):
    """Cumulative return summary for a model across rounds."""

    model_name: str
    rounds_with_data: int
    total_rounds: int
    simple_sum_pct: float
    compounded_pct: float
    round_details: list[RoundReturn]


def resolve_round_range(
    start_round: int,
    end_round: Optional[int],
    cfg: AppConfig,
    use_live: bool,
    client: Optional[NumeraiGraphQLClient] = None,
) -> list[int]:
    """Determine the list of rounds to process.

    Cache mode: end defaults to max cached round. Warns about missing rounds.
    Live mode: end defaults to latest round from API.
    """
    if use_live:
        if client is None:
            raise ValueError("Client required for live mode")
        if end_round is None:
            end_round = fetch_latest_round(client, cfg.tournament)
            logger.info(f"Latest round from API: {end_round}")
    else:
        cache_path = cfg.get_parquet_path()
        cached = get_cached_rounds(cache_path)
        if not cached:
            logger.error(f"No cached rounds found in {cache_path}. Run 'cache' first or use --live.")
            raise typer.Exit(1)
        if end_round is None:
            end_round = max(cached)
            logger.info(f"Latest cached round: {end_round}")
        missing = set(range(start_round, end_round + 1)) - cached
        if missing:
            logger.warning(f"Missing {len(missing)} rounds in cache: {sorted(missing)[:10]}...")

    return list(range(start_round, end_round + 1))


def gather_returns(
    rounds: list[int],
    pattern: re.Pattern,
    formula: FormulaBase,
    cfg: AppConfig,
    use_live: bool = False,
    client: Optional[NumeraiGraphQLClient] = None,
) -> dict[str, list[RoundReturn]]:
    """Gather per-round returns for all matching models across rounds."""
    model_rounds: dict[str, list[RoundReturn]] = {}
    cache_path = cfg.get_parquet_path()

    if not use_live:
        # Vectorized bulk path using polars — reads parquet once
        rows = gather_returns_bulk(cache_path, rounds, pattern, formula)
        for row in rows:
            rr = RoundReturn(
                round_number=int(row["round_number"]),
                score1=row.get("score1"),
                score2=row.get("score2"),
                payout_factor=float(row["payout_factor"]),
                return_pct=row.get("return_pct"),
            )
            model_rounds.setdefault(row["model_name"], []).append(rr)
        return model_rounds

    # Live API path — per-round queries
    for i, rnd in enumerate(rounds, 1):
        if i % 50 == 0:
            logger.info(f"Processing round {rnd} ({i}/{len(rounds)})")

        if client is None:
            raise ValueError("Client required for live API queries")
        results = fetch_rounddetails(client, cfg.tournament, rnd, pattern, formula)

        for r in results:
            rr = RoundReturn(
                round_number=rnd,
                score1=r.score1,
                score2=r.score2,
                payout_factor=r.payout_factor,
                return_pct=r.return_pct,
            )
            model_rounds.setdefault(r.model_name, []).append(rr)

    return model_rounds


def calculate_cumulative(
    model_rounds: dict[str, list[RoundReturn]],
    total_rounds: int,
) -> list[ModelCumulative]:
    """Calculate cumulative returns (simple + compounded) for each model."""
    results = []
    for name, rounds in model_rounds.items():
        simple_sum = 0.0
        compounded = 1.0
        valid_rounds = 0

        rounds.sort(key=lambda r: r.round_number)

        for rr in rounds:
            if rr.return_pct is not None:
                simple_sum += rr.return_pct
                compounded *= 1 + rr.return_pct / 100
                valid_rounds += 1

        results.append(
            ModelCumulative(
                model_name=name,
                rounds_with_data=valid_rounds,
                total_rounds=total_rounds,
                simple_sum_pct=simple_sum,
                compounded_pct=(compounded - 1) * 100,
                round_details=rounds,
            )
        )
    return results


def display_summary(
    cumulative: list[ModelCumulative],
    title: str,
    sort_desc: bool = True,
) -> None:
    """Display summary table with one row per model."""
    if not cumulative:
        typer.echo("No matching models found.")
        return

    cumulative.sort(key=lambda c: c.compounded_pct, reverse=sort_desc)

    rows = []
    for c in cumulative:
        rows.append([
            c.model_name,
            f"{c.rounds_with_data}/{c.total_rounds}",
            f"{c.simple_sum_pct:.4f}%",
            f"{c.compounded_pct:.4f}%",
        ])

    headers = ["Model", "Rounds", "Simple Sum %", "Compounded %"]
    typer.echo(f"\n{title}")
    typer.echo("=" * len(title))
    typer.echo(f"Models: {len(cumulative)}\n")
    typer.echo(tabulate(rows, headers=headers, tablefmt="grid"))


def display_detail(
    cum: ModelCumulative,
    title: str,
    column_headers: tuple[str, str],
) -> None:
    """Display per-round breakdown for a single model."""
    rows = []
    running_simple = 0.0
    running_compound = 1.0

    for rr in cum.round_details:
        ret = rr.return_pct
        if ret is not None:
            running_simple += ret
            running_compound *= 1 + ret / 100

        rows.append([
            rr.round_number,
            f"{rr.score1:.6f}" if rr.score1 is not None else "N/A",
            f"{rr.score2:.6f}" if rr.score2 is not None else "N/A",
            f"{rr.payout_factor:.6f}",
            f"{ret:.4f}%" if ret is not None else "N/A",
            f"{running_simple:.4f}%",
            f"{(running_compound - 1) * 100:.4f}%",
        ])

    headers = [
        "Round", column_headers[0], column_headers[1],
        "PF", "Return %", "Cum. Simple %", "Cum. Compound %",
    ]
    typer.echo(f"\n{title}")
    typer.echo("=" * len(title))
    typer.echo(tabulate(rows, headers=headers, tablefmt="grid"))

    # Final summary line
    typer.echo(
        f"\nTotal: {cum.rounds_with_data}/{cum.total_rounds} rounds | "
        f"Simple: {cum.simple_sum_pct:.4f}% | "
        f"Compounded: {cum.compounded_pct:.4f}%"
    )
