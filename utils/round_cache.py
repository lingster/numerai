"""
Numerai Round Performance - Parquet Cache

Read/write round details to a local parquet file for instant offline lookups.
"""

import math
import re
from pathlib import Path

import polars as pl
from loguru import logger

from round_config import FormulaBase, ModelResult

# Maps camelCase GraphQL keys to snake_case parquet column names
GRAPHQL_TO_COLUMN: dict[str, str] = {
    "id": "model_id",
    "modelName": "model_name",
    "mmc": "mmc",
    "v2Corr20": "v2_corr20",
    "mmc_60": "mmc_60",
    "corr_60": "corr_60",
    "bmc": "bmc",
    "fncV3": "fnc_v3",
    "cort20": "cort20",
    "mcwnm": "mcwnm",
    "apcwnm": "apcwnm",
    "corrWMetaModel": "corr_w_meta_model",
    "selectedStakeValue": "selected_stake_value",
    "payoutSettled": "payout_settled",
    "payoutPending": "payout_pending",
    "tc": "tc",
    "tcPercentile": "tc_percentile",
    "mmcPercentile": "mmc_percentile",
    "corr": "corr",
    "corr_20": "corr_20",
    "fnc": "fnc",
    "alpha": "alpha",
    "mpc": "mpc",
}


def load_parquet(path: Path) -> pl.DataFrame:
    """Read existing parquet file, return empty DataFrame if missing."""
    if path.exists():
        return pl.read_parquet(path)
    return pl.DataFrame()


def get_cached_rounds(path: Path) -> set[int]:
    """Return set of round numbers already present in the cache."""
    df = load_parquet(path)
    if df.is_empty() or "round_number" not in df.columns:
        return set()
    return set(df["round_number"].unique().to_list())


def build_cache_dataframe(
    round_number: int,
    tournament: int,
    payout_factor: float,
    raw_models: list[dict],
) -> pl.DataFrame:
    """Convert raw API response to a DataFrame with snake_case columns."""
    rows = []
    for m in raw_models:
        row: dict = {
            "round_number": round_number,
            "tournament": tournament,
            "payout_factor": payout_factor,
        }
        for gql_key, col_name in GRAPHQL_TO_COLUMN.items():
            row[col_name] = m.get(gql_key)
        rows.append(row)
    return pl.DataFrame(rows)


def save_to_parquet(
    new_df: pl.DataFrame,
    path: Path,
    rounds_to_replace: set[int],
) -> int:
    """Append/replace round data in the parquet file.

    Returns total row count after save.
    """
    existing = load_parquet(path)
    combined = _concat_aligned(existing, new_df, rounds_to_replace)
    combined.write_parquet(path)
    logger.info(f"Saved {len(combined)} rows to {path}")
    return len(combined)


def flush_to_parquet(
    existing_df: pl.DataFrame,
    new_dfs: list[pl.DataFrame],
    path: Path,
    rounds_to_replace: set[int] | None = None,
) -> pl.DataFrame:
    """Concat new round DataFrames onto existing, write to disk, return updated DataFrame."""
    if not new_dfs:
        return existing_df
    new_df = pl.concat(new_dfs, how="diagonal")
    combined = _concat_aligned(existing_df, new_df, rounds_to_replace or set())
    combined.write_parquet(path)
    logger.info(f"Flushed {len(new_dfs)} rounds → {len(combined)} total rows in {path}")
    return combined


def _concat_aligned(
    existing: pl.DataFrame,
    new_df: pl.DataFrame,
    rounds_to_replace: set[int],
) -> pl.DataFrame:
    """Merge new data into existing DataFrame, handling column alignment."""
    if not existing.is_empty() and rounds_to_replace:
        existing = existing.filter(~pl.col("round_number").is_in(list(rounds_to_replace)))

    if existing.is_empty():
        return new_df

    # Cast Null-typed columns in existing to match new_df schema before concat
    casts = [
        pl.col(c).cast(new_df.schema[c])
        for c in existing.columns
        if existing.schema[c] == pl.Null and c in new_df.schema and new_df.schema[c] != pl.Null
    ]
    if casts:
        existing = existing.with_columns(casts)

    # diagonal concat handles mismatched columns by filling missing with null
    return pl.concat([existing, new_df], how="diagonal")


def read_cache_for_round(
    path: Path,
    round_number: int,
    pattern: re.Pattern,
    formula: FormulaBase,
) -> list[ModelResult]:
    """Read cached round data, rank all models by return %, then filter by regex."""
    df = load_parquet(path)
    return read_round_from_df(df, path, round_number, pattern, formula)


def read_round_from_df(
    df: pl.DataFrame,
    source: Path | str,
    round_number: int,
    pattern: re.Pattern,
    formula: FormulaBase,
) -> list[ModelResult]:
    """Filter a pre-loaded DataFrame for one round, rank, and apply regex."""
    if df.is_empty():
        logger.error(f"Cache {source} is empty or missing")
        return []

    if "round_number" not in df.columns:
        logger.error("Cache has no round_number column")
        return []

    df_round = df.filter(pl.col("round_number") == round_number)
    if df_round.is_empty():
        logger.error(f"Round {round_number} not found in cache")
        return []

    pf = float(df_round["payout_factor"][0])
    col1, col2 = formula.cache_score_columns

    # Calculate return for ALL models, then rank
    all_rows: list[tuple[str, float | None, float | None, float | None]] = []
    for row in df_round.iter_rows(named=True):
        name = str(row.get("model_name", ""))
        s1 = _safe_float(row.get(col1))
        s2 = _safe_float(row.get(col2))
        ret = formula.calculate_return(s1, s2, pf)
        all_rows.append((name, s1, s2, ret))

    all_rows.sort(key=lambda x: x[3] if x[3] is not None else float("-inf"), reverse=True)

    total = len(all_rows)
    filtered: list[ModelResult] = []
    for rank, (name, s1, s2, ret) in enumerate(all_rows, 1):
        if not name or not pattern.search(name):
            continue
        filtered.append(
            ModelResult(
                model_name=name,
                score1=s1,
                score2=s2,
                payout_factor=pf,
                return_pct=ret,
                rank=rank,
                total_models=total,
            )
        )
    return filtered


def gather_returns_bulk(
    path: Path,
    rounds: list[int],
    pattern: re.Pattern,
    formula: FormulaBase,
) -> list[dict]:
    """Vectorized bulk computation of returns using polars for speed.

    Reads parquet directly with polars, computes returns across all rounds
    in a single vectorized pass, and filters by model regex.

    Returns list of dicts with keys: round_number, model_name, score1, score2,
    payout_factor, return_pct.
    """
    if not path.exists():
        logger.error(f"Cache file {path} not found")
        return []

    col1, col2 = formula.cache_score_columns
    needed_cols = ["round_number", "model_name", "payout_factor", col1, col2]

    # Read only needed columns from parquet
    lf = pl.scan_parquet(path).select(needed_cols)

    # Filter to requested rounds and apply regex
    lf = lf.filter(
        pl.col("round_number").is_in(rounds)
        & pl.col("model_name").str.contains(pattern.pattern, literal=False)
    )

    # Compute return: clip(pf * (m1*s1 + m2*s2), clip_min, clip_max) * 100
    s1 = pl.col(col1).cast(pl.Float64, strict=False)
    s2 = pl.col(col2).cast(pl.Float64, strict=False)
    pf = pl.col("payout_factor").cast(pl.Float64, strict=False)

    raw = pf * (formula.multiplier1 * s1 + formula.multiplier2 * s2)
    clipped = raw.clip(formula.clip_min, formula.clip_max)
    ret = clipped * 100

    result = lf.with_columns(
        s1.alias("score1"),
        s2.alias("score2"),
        pl.when(s1.is_not_null() & s2.is_not_null())
        .then(ret)
        .otherwise(None)
        .alias("return_pct"),
    ).select(
        "round_number", "model_name", "score1", "score2", "payout_factor", "return_pct"
    ).collect()

    return result.to_dicts()


def _safe_float(val) -> float | None:
    """Convert a value to float, returning None for NaN/None."""
    if val is None:
        return None
    if isinstance(val, float) and math.isnan(val):
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None
