#!/usr/bin/env python3
"""
Numerai GraphQL API - Model Performance Example

Fetches model performance history for a given username and tournament.

Usage:
    python get_model_performance.py --username myuser --rounds 20 --tournament 8

Requirements:
    pip install httpx
"""

import argparse
import httpx
import json
from typing import Optional

API_URL = "https://api-tournament.numer.ai/"


def gql(query: str, variables: Optional[dict] = None) -> dict:
    """Execute a GraphQL query against the Numerai API."""
    resp = httpx.post(
        API_URL,
        json={"query": query, "variables": variables or {}},
        timeout=30.0
    )
    resp.raise_for_status()
    result = resp.json()
    if "errors" in result:
        raise ValueError(f"GraphQL errors: {result['errors']}")
    return result["data"]


def get_user_models(username: str, tournament: int = 8) -> list:
    """Get all models for a user in a given tournament."""
    query = """
    query($username: String!, $tournament: Int!) {
      accountProfile(username: $username, tournament: $tournament) {
        username
        displayName
        models {
          id
          displayName
          tournament
          startDate
          stake
          return1y
          corrRep
          mmcRep
        }
      }
    }
    """
    data = gql(query, {"username": username, "tournament": tournament})
    profile = data["accountProfile"]
    print(f"User: {profile['displayName'] or profile['username']}")
    return profile["models"]


def get_model_performance(model_id: str, last_n_rounds: int = 20, tournament: int = 8) -> list:
    """Get round-by-round performance for a model."""
    query = """
    query($modelId: String!, $lastNRounds: Int!, $tournament: Int!) {
      v2RoundModelPerformances(
        modelId: $modelId,
        lastNRounds: $lastNRounds,
        tournament: $tournament,
        resolvedOnly: true
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
        roundResolveTime
        roundPayoutFactor
      }
    }
    """
    data = gql(query, {
        "modelId": model_id,
        "lastNRounds": last_n_rounds,
        "tournament": tournament
    })
    return data["v2RoundModelPerformances"]


def get_nmr_price() -> float:
    """Get current NMR/USD price."""
    query = """
    query {
      latestCurrencyPrice(targetSymbol: "USD", baseSymbol: "NMR") {
        price
        lastUpdated
      }
    }
    """
    data = gql(query)
    return float(data["latestCurrencyPrice"]["price"])


def print_performance_table(model_name: str, performances: list, nmr_price: float):
    """Print a formatted performance table."""
    print(f"\n{'='*80}")
    print(f"Model: {model_name}")
    print(f"NMR Price: ${nmr_price:.2f}")
    print(f"{'='*80}")
    print(f"{'Round':>7} {'Corr':>8} {'Corr%':>7} {'MMC':>8} {'MMC%':>7} {'Stake':>8} {'Payout':>10}")
    print(f"{'-'*7} {'-'*8} {'-'*7} {'-'*8} {'-'*7} {'-'*8} {'-'*10}")

    total_payout = 0.0
    for p in sorted(performances, key=lambda x: x["roundNumber"]):
        corr = p.get("corr") or 0
        mmc = p.get("mmc") or 0
        corr_pct = (p.get("corrPercentile") or 0) * 100
        mmc_pct = (p.get("mmcPercentile") or 0) * 100
        stake = float(p.get("selectedStakeValue") or 0)
        payout = float(p.get("payout") or 0)
        total_payout += payout

        payout_usd = payout * nmr_price
        print(
            f"{p['roundNumber']:>7} "
            f"{corr:>8.4f} "
            f"{corr_pct:>6.1f}% "
            f"{mmc:>8.4f} "
            f"{mmc_pct:>6.1f}% "
            f"{stake:>8.2f} "
            f"{payout:>+8.4f} NMR"
        )

    print(f"{'-'*80}")
    print(f"Total payout: {total_payout:+.4f} NMR (${total_payout * nmr_price:.2f})")


def main():
    parser = argparse.ArgumentParser(description="Fetch Numerai model performance")
    parser.add_argument("--username", required=True, help="Numerai username")
    parser.add_argument("--rounds", type=int, default=20, help="Number of recent rounds (default: 20)")
    parser.add_argument("--tournament", type=int, default=8, choices=[8, 11, 12],
                        help="Tournament ID: 8=Classic, 11=Signals, 12=Crypto (default: 8)")
    parser.add_argument("--model", help="Specific model name (uses first model if not specified)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    # Get models
    models = get_user_models(args.username, args.tournament)
    if not models:
        print(f"No models found for {args.username} in tournament {args.tournament}")
        return

    # Select model
    if args.model:
        model = next((m for m in models if m["displayName"] == args.model), None)
        if not model:
            print(f"Model '{args.model}' not found. Available models:")
            for m in models:
                print(f"  - {m['displayName']}")
            return
    else:
        model = models[0]
        if len(models) > 1:
            print(f"Multiple models found, using '{model['displayName']}'. Use --model to specify.")

    print(f"Fetching performance for model: {model['displayName']} (ID: {model['id']})")

    # Get performance
    performances = get_model_performance(model["id"], args.rounds, args.tournament)

    if args.json:
        print(json.dumps(performances, indent=2))
        return

    # Get NMR price for USD conversion
    try:
        nmr_price = get_nmr_price()
    except Exception:
        nmr_price = 0.0

    print_performance_table(model["displayName"], performances, nmr_price)


if __name__ == "__main__":
    main()
