#!/usr/bin/env python3
"""
Numerai GraphQL MCP server.

Exposes common Numerai GraphQL queries as MCP tools.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from typing import Any, Dict, Optional

import httpx
from mcp.server.fastmcp import FastMCP


NUMERAI_API_URL = "https://api-tournament.numer.ai/"

_logger = logging.getLogger("numerai-mcp")
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

_http_client = httpx.Client(timeout=30.0)

mcp = FastMCP("numerai-graphql")


def _auth_header() -> Optional[str]:
    public_id = os.getenv("NUMERAI_PUBLIC_ID") or os.getenv("NUMERAI_API_PUBLIC_ID")
    secret_key = os.getenv("NUMERAI_SECRET_KEY") or os.getenv("NUMERAI_API_SECRET_KEY")
    if public_id and secret_key:
        return f"Token {public_id}${secret_key}"
    return None


def _build_headers(use_auth: bool) -> Dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if use_auth:
        auth_header = _auth_header()
        if auth_header:
            headers["Authorization"] = auth_header
    return headers


def _post_graphql(query: str, variables: Optional[Dict[str, Any]] = None, use_auth: bool = True) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"query": query}
    if variables is not None:
        payload["variables"] = variables

    try:
        response = _http_client.post(NUMERAI_API_URL, headers=_build_headers(use_auth), json=payload)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as exc:
        _logger.error("HTTP error from Numerai API: %s", exc)
        return {
            "http_error": "HTTPStatusError",
            "status_code": exc.response.status_code,
            "text": exc.response.text,
        }
    except httpx.RequestError as exc:
        _logger.error("Request error to Numerai API: %s", exc)
        return {"http_error": "RequestError", "message": str(exc)}
    except json.JSONDecodeError as exc:
        _logger.error("Failed to decode JSON response: %s", exc)
        return {"http_error": "JSONDecodeError", "message": str(exc)}


@mcp.tool()
def auth_status() -> Dict[str, Any]:
    """Check whether Numerai auth environment variables are set."""
    public_id = os.getenv("NUMERAI_PUBLIC_ID") or os.getenv("NUMERAI_API_PUBLIC_ID")
    secret_key = os.getenv("NUMERAI_SECRET_KEY") or os.getenv("NUMERAI_API_SECRET_KEY")
    return {
        "has_public_id": bool(public_id),
        "has_secret_key": bool(secret_key),
        "uses_auth_header": bool(_auth_header()),
    }


@mcp.tool()
def graphql_query(query: str, variables_json: Optional[str] = None, use_auth: bool = True) -> Dict[str, Any]:
    """
    Execute an arbitrary GraphQL query.

    Args:
        query: The GraphQL query string.
        variables_json: Optional JSON string of variables to pass.
        use_auth: Whether to include auth headers if available.
    """
    variables = None
    if variables_json:
        variables = json.loads(variables_json)
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def list_tournaments(use_auth: bool = False) -> Dict[str, Any]:
    """List available tournaments."""
    query = """
    {
      tournaments {
        id
        name
        tournament
        active
      }
    }
    """
    return _post_graphql(query, use_auth=use_auth)


@mcp.tool()
def rounds(
    tournament: int = 8,
    limit: Optional[int] = 5,
    number: Optional[int] = None,
    status: Optional[str] = None,
    target: Optional[str] = None,
    use_auth: bool = False,
) -> Dict[str, Any]:
    """Get round information with filtering options."""
    query = """
    query Rounds($tournament: Int, $limit: Int, $number: Int, $status: RoundStatus, $target: String) {
      rounds(tournament: $tournament, limit: $limit, number: $number, status: $status, target: $target) {
        number
        openTime
        closeTime
        resolveTime
        scoreTime
        resolvedGeneral
        resolvedStaking
        tournament
        target
        numTickers
        payoutFactor
      }
    }
    """
    variables = {
        "tournament": tournament,
        "limit": limit,
        "number": number,
        "status": status,
        "target": target,
    }
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def account(use_auth: bool = True) -> Dict[str, Any]:
    """Get the authenticated account details (requires auth)."""
    query = """
    {
      account {
        id
        username
        displayName
        email
        availableNmr
        totalStakeValues {
          value
          date
        }
        models {
          id
          name
          tournament
          returns {
            oneDay
            oneWeek
            oneMonth
            threeMonths
            oneYear
            allTime
          }
        }
      }
    }
    """
    return _post_graphql(query, use_auth=use_auth)


@mcp.tool()
def account_profile(username: str, tournament: int = 8, use_auth: bool = False) -> Dict[str, Any]:
    """Get public profile information for a user."""
    query = """
    query AccountProfile($username: String!, $tournament: Int) {
      accountProfile(username: $username, tournament: $tournament) {
        id
        username
        displayName
        bio
        location
        models {
          id
          displayName
          tournament
        }
        returns {
          oneDay
          oneWeek
          oneMonth
          threeMonths
          oneYear
          allTime
        }
      }
    }
    """
    variables = {"username": username, "tournament": tournament}
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def account_leaderboard(
    tournament: int = 8,
    limit: int = 10,
    offset: int = 0,
    order_by: str = "corr",
    direction: str = "desc",
    filter_by: Optional[str] = None,
    use_auth: bool = False,
) -> Dict[str, Any]:
    """Get leaderboard rankings with filtering and sorting."""
    query = """
    query AccountLeaderboard(
      $tournament: Int,
      $limit: Int,
      $offset: Int,
      $orderBy: String,
      $direction: String,
      $filterBy: String
    ) {
      accountLeaderboard(
        tournament: $tournament,
        limit: $limit,
        offset: $offset,
        orderBy: $orderBy,
        direction: $direction,
        filterBy: $filterBy
      ) {
        username
        displayName
        rank
        corr
        corr60
        mmc
        mmc60
        nmrStaked
        return1y
        return3m
        returnAllTime
      }
    }
    """
    variables = {
        "tournament": tournament,
        "limit": limit,
        "offset": offset,
        "orderBy": order_by,
        "direction": direction,
        "filterBy": filter_by,
    }
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def model(model_id: str, use_auth: bool = False) -> Dict[str, Any]:
    """Get detailed information about a specific model."""
    query = """
    query Model($modelId: ID!) {
      model(modelId: $modelId) {
        id
        name
        username
        tournament
        description
        computeEnabled
        returns {
          oneDay
          oneWeek
          oneMonth
          threeMonths
          oneYear
          allTime
        }
        returnsValues {
          date
          value
        }
        latestSubmissions {
          id
          filename
          insertedAt
          round {
            number
            tournament
          }
        }
      }
    }
    """
    variables = {"modelId": model_id}
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def submissions(model_id: str, use_auth: bool = False) -> Dict[str, Any]:
    """Get submission history for a model."""
    query = """
    query Submissions($modelId: ID!) {
      submissions(modelId: $modelId) {
        id
        filename
        insertedAt
        round {
          number
          openTime
          closeTime
          tournament
        }
        validationCorrelation
        validationMmc
      }
    }
    """
    variables = {"modelId": model_id}
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def v2_round_model_performances(
    model_id: str,
    tournament: int = 8,
    last_n_rounds: int = 20,
    round_number_gte: Optional[int] = None,
    round_number_lte: Optional[int] = None,
    resolved_only: Optional[bool] = None,
    submitted_only: Optional[bool] = None,
    use_auth: bool = False,
) -> Dict[str, Any]:
    """Get performance metrics for a model across rounds."""
    query = """
    query V2RoundModelPerformances(
      $modelId: String!,
      $tournament: Int,
      $lastNRounds: Int,
      $roundNumberGte: Int,
      $roundNumberLte: Int,
      $resolvedOnly: Boolean,
      $submittedOnly: Boolean
    ) {
      v2RoundModelPerformances(
        modelId: $modelId,
        tournament: $tournament,
        lastNRounds: $lastNRounds,
        roundNumberGte: $roundNumberGte,
        roundNumberLte: $roundNumberLte,
        resolvedOnly: $resolvedOnly,
        submittedOnly: $submittedOnly
      ) {
        roundNumber
        corr
        mmc
        fnc
        tc
        corrPercentile
        mmcPercentile
        roundResolved
        selectedStakeValue
        payout
      }
    }
    """
    variables = {
        "modelId": model_id,
        "tournament": tournament,
        "lastNRounds": last_n_rounds,
        "roundNumberGte": round_number_gte,
        "roundNumberLte": round_number_lte,
        "resolvedOnly": resolved_only,
        "submittedOnly": submitted_only,
    }
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def dataset(tournament: int, round_number: int, filename: str, use_auth: bool = False) -> Dict[str, Any]:
    """Get information about a dataset download."""
    query = """
    query Dataset($tournament: Int!, $round: Int!, $filename: String!) {
      dataset(tournament: $tournament, round: $round, filename: $filename) {
        id
        filename
        round {
          number
          tournament
        }
        url
      }
    }
    """
    variables = {"tournament": tournament, "round": round_number, "filename": filename}
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def list_datasets(tournament: int, round_number: int, use_auth: bool = False) -> Dict[str, Any]:
    """List datasets for a tournament/round."""
    query = """
    query ListDatasets($tournament: Int!, $round: Int!) {
      listDatasets(tournament: $tournament, round: $round) {
        filename
        url
      }
    }
    """
    variables = {"tournament": tournament, "round": round_number}
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def latest_currency_price(target_symbol: str, base_symbol: str = "NMR", use_auth: bool = False) -> Dict[str, Any]:
    """Get the latest currency price for NMR vs a target symbol."""
    query = """
    query LatestCurrencyPrice($targetSymbol: String!, $baseSymbol: String!) {
      latestCurrencyPrice(targetSymbol: $targetSymbol, baseSymbol: $baseSymbol) {
        lastUpdated
        baseSymbol
        targetSymbol
        price
      }
    }
    """
    variables = {"targetSymbol": target_symbol, "baseSymbol": base_symbol}
    return _post_graphql(query, variables=variables, use_auth=use_auth)


@mcp.tool()
def round_details(
    tournament: int,
    round_number: int,
    include_models: bool = False,
    include_histograms: bool = False,
    use_auth: bool = False,
) -> Dict[str, Any]:
    """Get detailed round information; optional models and histogram data."""
    query = """
    query RoundDetails($tournament: Int!, $roundNumber: Int!, $includeModels: Boolean!, $includeHistograms: Boolean!) {
      roundDetails(tournament: $tournament, roundNumber: $roundNumber) {
        roundNumber
        roundId
        tournament
        status
        roundTarget
        openTime
        closeTime
        closeStakingTime
        scoresUpdatedTime
        roundResolveTime
        payoutFactor
        totalPayout
        totalEarned
        totalBurned
        totalAtStake
        totalStakes
        models @include(if: $includeModels) {
          id
          modelName
          profileUrl
          team
          computeEnabled
          selectedStakeValue
          payoutPending
          payoutSettled
          tc
          tcPercentile
          corrWMetaModel
          fnc
          corr20: corr_20
          v2_corr20: v2Corr20
          corr60: corr_60
          mmc60: mmc_60
          cort20
          fnc_v3: fncV3
          mcwnm
          apcwnm
          mmc
          mmcPercentile
          bmc
          corr
          corr_v4: corrV4
          ric
          fnc_v4: fncV4
          ic_v2: icV2
          cwsnmm
          mcwsm
          apcwsm
          alpha
          mpc
        }
        allHistogramData @include(if: $includeHistograms) {
          bins
          counts
        }
        stakedHistogramData @include(if: $includeHistograms) {
          bins
          counts
        }
      }
    }
    """
    variables = {
        "tournament": tournament,
        "roundNumber": round_number,
        "includeModels": include_models,
        "includeHistograms": include_histograms,
    }
    return _post_graphql(query, variables=variables, use_auth=use_auth)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
