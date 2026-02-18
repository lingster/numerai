"""
Numerai Round Performance - Display Helpers

Table formatting and display functions for round performance results.
"""

from typing import Optional

import typer
from tabulate import tabulate

from round_config import AppConfig, ModelResult, Tournament

SORT_KEYS = {
    "return_pct": lambda r: r.return_pct if r.return_pct is not None else float("-inf"),
    "mmc20": lambda r: r.score1 if r.score1 is not None else float("-inf"),
    "corr20": lambda r: r.score2 if r.score2 is not None else float("-inf"),
    "model_name": lambda r: r.model_name.lower(),
}


def display_results(
    results: list[ModelResult],
    title: str,
    sort_by: str = "return_pct",
    sort_desc: bool = True,
    column_headers: tuple[str, str] = ("MMC20", "CORR20"),
) -> None:
    """Display results as a formatted table sorted by the chosen metric"""
    if not results:
        typer.echo("No matching models found.")
        return

    sort_fn = SORT_KEYS.get(sort_by, SORT_KEYS["return_pct"])
    results.sort(key=sort_fn, reverse=sort_desc)

    has_rank = any(r.rank is not None for r in results)
    total = results[0].total_models if has_rank else None

    rows = []
    for r in results:
        row = [r.model_name]
        if has_rank:
            row.append(f"{r.rank}/{total}" if r.rank is not None else "N/A")
        row.extend([
            f"{r.score1:.6f}" if r.score1 is not None else "N/A",
            f"{r.score2:.6f}" if r.score2 is not None else "N/A",
            f"{r.payout_factor:.6f}",
            f"{r.return_pct:.4f}%" if r.return_pct is not None else "N/A",
        ])
        rows.append(row)

    headers = ["Model"]
    if has_rank:
        headers.append("Rank")
    headers.extend([column_headers[0], column_headers[1], "Payout Factor", "Return %"])

    typer.echo(f"\n{title}")
    typer.echo("=" * len(title))
    typer.echo(f"Models matched: {len(results)}\n")
    typer.echo(tabulate(rows, headers=headers, tablefmt="grid"))


def display_timing(t_rd: float, t_pm: float, n_rd: int, n_pm: int) -> None:
    """Display timing comparison between both methods"""
    diff = abs(t_rd - t_pm)
    base = min(t_rd, t_pm) if min(t_rd, t_pm) > 0 else 1
    pct = (diff / base) * 100
    faster = "rounddetails" if t_rd <= t_pm else "permodel"

    typer.echo(f"\n{'=' * 60}")
    typer.echo(f"{'Timing Comparison':^60}")
    typer.echo(f"{'=' * 60}")
    typer.echo(f"  rounddetails : {t_rd:.3f}s  ({n_rd} results)")
    typer.echo(f"  permodel     : {t_pm:.3f}s  ({n_pm} results)")
    typer.echo(f"  Difference   : {diff:.3f}s  ({pct:.1f}%)")
    typer.echo(f"  Winner       : {faster}")


def parse_tournament(value: Optional[str]) -> Optional[Tournament]:
    """Parse tournament string (classic/signals/crypto or 8/11/12) to enum"""
    if value is None:
        return None
    try:
        return Tournament[value.upper()]
    except KeyError:
        pass
    try:
        return Tournament(int(value))
    except (ValueError, KeyError):
        raise typer.BadParameter(
            f"Invalid tournament '{value}'. Use classic/signals/crypto or 8/11/12"
        )


def apply_overrides(cfg: AppConfig, **kwargs) -> None:
    """Apply non-None CLI overrides to config"""
    if kwargs.get("tournament") is not None:
        cfg.tournament = parse_tournament(kwargs["tournament"])
    formula = cfg.get_formula()
    if kwargs.get("mmc_mult") is not None and hasattr(formula, "mmc_multiplier"):
        formula.mmc_multiplier = kwargs["mmc_mult"]
    if kwargs.get("corr_mult") is not None and hasattr(formula, "corr_multiplier"):
        formula.corr_multiplier = kwargs["corr_mult"]
    if kwargs.get("method") is not None:
        cfg.method = kwargs["method"]
    if kwargs.get("both"):
        cfg.method = "both"
    if kwargs.get("sort_by") is not None:
        cfg.sort_by = kwargs["sort_by"]
    if kwargs.get("descending") is not None:
        cfg.sort_desc = kwargs["descending"]
    if kwargs.get("max_models") is not None:
        cfg.max_models = kwargs["max_models"]
    if kwargs.get("parquet_path") is not None:
        cfg.parquet_path = kwargs["parquet_path"]
