"""
Numerai Round Performance - Data Fetchers

Two methods for fetching round model performance data:
- rounddetails: Single bulk query, filter locally
- permodel: Light model list + individual v2RoundModelPerformances queries
"""

import re
from typing import Optional

from loguru import logger

from numerai_client import NumeraiGraphQLClient
from round_config import FormulaBase, ModelResult


# --- GraphQL Queries ---

ROUND_DETAILS_FULL = """
query roundDetails($tournament: Int!, $roundNumber: Int!) {
  roundDetails(tournament: $tournament, roundNumber: $roundNumber) {
    payoutFactor
    models { id modelName mmc v2Corr20 corr alpha mpc }
  }
}
"""

ROUND_DETAILS_LIGHT = """
query roundDetails($tournament: Int!, $roundNumber: Int!) {
  roundDetails(tournament: $tournament, roundNumber: $roundNumber) {
    payoutFactor
    models { id modelName }
  }
}
"""

ROUND_DETAILS_CACHE = """
query roundDetailsCache($tournament: Int!, $roundNumber: Int!) {
  roundDetails(tournament: $tournament, roundNumber: $roundNumber) {
    payoutFactor
    models {
      id modelName mmc v2Corr20 mmc_60 corr_60
      bmc fncV3 cort20 mcwnm apcwnm corrWMetaModel
      selectedStakeValue payoutSettled payoutPending
      tc tcPercentile mmcPercentile corr corr_20 fnc
      alpha mpc
    }
  }
}
"""

LATEST_ROUND_QUERY = """
query latestRound($tournament: Int!) {
  rounds(tournament: $tournament, limit: 1) {
    number
  }
}
"""

MODEL_PERF_QUERY = """
query modelPerf($modelId: String!, $tournament: Int!, $roundNumber__eq: Int!) {
  v2RoundModelPerformances(
    modelId: $modelId, tournament: $tournament, roundNumber__eq: $roundNumber__eq
  ) {
    roundNumber
    submissionScores { displayName value }
  }
}
"""


def _find_score(scores: list[dict], names: tuple[str, ...]) -> Optional[float]:
    """Extract first matching score from submissionScores array"""
    score_map = {s["displayName"]: s.get("value") for s in scores}
    for name in names:
        if name in score_map:
            return score_map[name]
    return None


# --- Method 1: Full roundDetails ---


def _rank_and_filter(
    models: list[dict],
    pf: float,
    pattern: re.Pattern,
    formula: FormulaBase,
) -> list[ModelResult]:
    """Calculate return for all models, rank by return %, then filter by regex."""
    all_results: list[tuple[str, float | None, float | None, float | None]] = []
    for m in models:
        name = m.get("modelName", "")
        s1, s2 = formula.extract_scores(m)
        ret = formula.calculate_return(s1, s2, pf)
        all_results.append((name, s1, s2, ret))

    # Sort all models by return % descending (None goes last)
    all_results.sort(key=lambda x: x[3] if x[3] is not None else float("-inf"), reverse=True)

    total = len(all_results)
    filtered: list[ModelResult] = []
    for rank, (name, s1, s2, ret) in enumerate(all_results, 1):
        if not pattern.search(name):
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


def fetch_rounddetails(
    client: NumeraiGraphQLClient,
    tournament: int,
    round_number: int,
    pattern: re.Pattern,
    formula: FormulaBase,
) -> list[ModelResult]:
    """Single bulk query for all model data, filtered locally by regex"""
    result = client.query(
        ROUND_DETAILS_FULL,
        {"tournament": tournament, "roundNumber": round_number},
    )
    rd = result.get("roundDetails")
    if not rd:
        logger.error("No round details returned")
        return []

    pf = float(rd.get("payoutFactor", 0))
    models = rd.get("models") or []
    logger.info(f"roundDetails returned {len(models)} models, payout_factor={pf:.6f}")

    return _rank_and_filter(models, pf, pattern, formula)


# --- Method 2: Light roundDetails + per-model queries ---


def fetch_permodel(
    client: NumeraiGraphQLClient,
    tournament: int,
    round_number: int,
    pattern: re.Pattern,
    formula: FormulaBase,
    max_models: int = 100,
) -> list[ModelResult]:
    """Light model list query, then individual v2RoundModelPerformances per match"""
    result = client.query(
        ROUND_DETAILS_LIGHT,
        {"tournament": tournament, "roundNumber": round_number},
    )
    rd = result.get("roundDetails")
    if not rd:
        logger.error("No round details returned")
        return []

    pf = float(rd.get("payoutFactor", 0))
    all_models = rd.get("models") or []
    matched = [
        (m["modelName"], m["id"])
        for m in all_models
        if m.get("modelName") and pattern.search(m["modelName"])
    ]

    if len(matched) > max_models:
        logger.warning(f"Regex matched {len(matched)} models, capping at {max_models}")
        matched = matched[:max_models]
    logger.info(f"Querying {len(matched)} individual models via v2RoundModelPerformances")

    s1_names, s2_names = formula.score_display_names
    results = []
    for i, (name, model_id) in enumerate(matched, 1):
        if i % 25 == 0:
            logger.info(f"Progress: {i}/{len(matched)} models queried")
        perf = client.query(
            MODEL_PERF_QUERY,
            {"modelId": model_id, "tournament": tournament, "roundNumber__eq": round_number},
        )
        perfs = perf.get("v2RoundModelPerformances") or []
        scores = perfs[0].get("submissionScores", []) if perfs else []
        s1 = _find_score(scores, s1_names)
        s2 = _find_score(scores, s2_names)
        results.append(
            ModelResult(
                model_name=name,
                score1=s1,
                score2=s2,
                payout_factor=pf,
                return_pct=formula.calculate_return(s1, s2, pf),
            )
        )
    return results


# --- Cache support queries ---


def fetch_latest_round(client: NumeraiGraphQLClient, tournament: int) -> int:
    """Fetch the latest round number for a tournament"""
    result = client.query(LATEST_ROUND_QUERY, {"tournament": tournament})
    rounds = result.get("rounds") or []
    if not rounds:
        raise ValueError(f"No rounds found for tournament {tournament}")
    return int(rounds[0]["number"])


def fetch_rounddetails_raw(
    client: NumeraiGraphQLClient,
    tournament: int,
    round_number: int,
) -> tuple[float, list[dict]]:
    """Fetch raw round details with all model fields for caching.

    Returns (payout_factor, raw_models_list).
    """
    result = client.query(
        ROUND_DETAILS_CACHE,
        {"tournament": tournament, "roundNumber": round_number},
    )
    rd = result.get("roundDetails")
    if not rd:
        logger.warning(f"No round details for round {round_number}")
        return 0.0, []

    pf = float(rd.get("payoutFactor", 0))
    models = rd.get("models") or []
    logger.info(f"Round {round_number}: {len(models)} models, payout_factor={pf:.6f}")
    return pf, models
