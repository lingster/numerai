"""
Numerai Round Performance - Position Tracking

Compute and plot model rank/percentile position across rounds from the parquet cache.
"""

import re

import polars as pl
import typer
from loguru import logger

from round_cache import load_parquet
from round_config import FormulaBase


def get_metric_label(formula: FormulaBase, metric: str) -> str:
    """Return a human-readable label for the chosen metric."""
    if metric == "return_pct":
        return "Return %"
    if metric == "score1":
        return formula.column_headers[0]
    return formula.column_headers[1]


def compute_positions(
    cache_path: "Path",
    rounds: list[int],
    pattern: re.Pattern,
    formula: FormulaBase,
    metric: str,
) -> pl.DataFrame:
    """Compute rank and percentile for matched models across rounds.

    Returns DataFrame with columns:
        round_number, model_name, metric_value, rank, total_models, percentile
    """
    df = load_parquet(cache_path)
    if df.is_empty():
        logger.error(f"Cache {cache_path} is empty or missing")
        return pl.DataFrame()

    col1, col2 = formula.cache_score_columns

    # Filter to requested rounds
    df = df.filter(pl.col("round_number").is_in(rounds))
    if df.is_empty():
        logger.error("No data for requested rounds in cache")
        return pl.DataFrame()

    # Build metric column
    s1 = pl.col(col1).cast(pl.Float64, strict=False)
    s2 = pl.col(col2).cast(pl.Float64, strict=False)
    pf = pl.col("payout_factor").cast(pl.Float64, strict=False)

    if metric == "return_pct":
        raw = pf * (formula.multiplier1 * s1 + formula.multiplier2 * s2)
        metric_expr = raw.clip(formula.clip_min, formula.clip_max) * 100
        # Only valid when both scores present
        metric_expr = (
            pl.when(s1.is_not_null() & s2.is_not_null())
            .then(metric_expr)
            .otherwise(None)
        )
    elif metric == "score1":
        metric_expr = s1
    else:
        metric_expr = s2

    df = df.with_columns(metric_expr.alias("metric_value"))

    # Drop rows without a metric value (can't rank them)
    df = df.filter(pl.col("metric_value").is_not_null())

    # Rank within each round (higher metric = rank 1)
    df = df.with_columns(
        pl.col("metric_value")
        .rank("ordinal", descending=True)
        .over("round_number")
        .alias("rank"),
        pl.col("metric_value")
        .count()
        .over("round_number")
        .alias("total_models"),
    )

    # Percentile: rank / total * 100 (lower = better)
    df = df.with_columns(
        (pl.col("rank") / pl.col("total_models") * 100).alias("percentile")
    )

    # Filter to matched models
    df = df.filter(
        pl.col("model_name").str.contains(pattern.pattern, literal=False)
    )

    return df.select(
        "round_number", "model_name", "metric_value", "rank", "total_models", "percentile"
    ).sort("model_name", "round_number")


def plot_positions(
    df: pl.DataFrame,
    title: str,
    width: int = 120,
    height: int = 30,
) -> None:
    """Plot percentile position over rounds for each model."""
    import plotext as plt

    models = df["model_name"].unique().sort().to_list()
    colors = ["blue", "red", "green", "orange", "magenta", "cyan", "yellow", "white"]

    plt.clear_figure()
    plt.plot_size(width, height)

    for i, model in enumerate(models):
        mdf = df.filter(pl.col("model_name") == model).sort("round_number")
        rounds = mdf["round_number"].to_list()
        pcts = mdf["percentile"].to_list()
        color = colors[i % len(colors)]
        plt.plot(rounds, pcts, marker="braille", color=color, label=model)

    plt.title(title)
    plt.xlabel("Round Number")
    plt.ylabel("Top % (lower = better)")
    plt.show()

    # Print summary stats
    summary = (
        df.group_by("model_name")
        .agg(
            pl.col("percentile").mean().alias("avg_pct"),
            pl.col("percentile").min().alias("best_pct"),
            pl.col("percentile").max().alias("worst_pct"),
            pl.col("percentile").last().alias("latest_pct"),
            pl.col("round_number").count().alias("rounds"),
        )
        .sort("avg_pct")
    )
    typer.echo(f"\n{'Model':<30} {'Avg%':>7} {'Best%':>7} {'Worst%':>8} {'Latest%':>9} {'Rounds':>7}")
    typer.echo("-" * 70)
    for row in summary.iter_rows(named=True):
        typer.echo(
            f"{row['model_name']:<30} {row['avg_pct']:>7.1f} {row['best_pct']:>7.1f} "
            f"{row['worst_pct']:>8.1f} {row['latest_pct']:>9.1f} {row['rounds']:>7}"
        )
