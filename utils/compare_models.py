#!/usr/bin/env python3
"""
Numerai Model Comparison Tool

This script provides two main commands:
1. Compare historical performance data between two Numerai models
2. Get a list of your models with their UUIDs

Usage:
    python compare_models.py compare model_a_identifier model_b_identifier [--rounds 20] [--public-id YOUR_ID] [--secret-key YOUR_KEY]
    python compare_models.py get-models [--public-id YOUR_ID] [--secret-key YOUR_KEY]

Model identifiers can be either UUIDs or model names (for your own models).

Authentication:
    Either provide --public-id and --secret-key, or set environment variables:
    export NUMER_PUBLIC_API_KEY=your_public_id
    export NUMER_SECRET_API_KEY=your_secret_key

    Get your API keys from: https://numer.ai/account

Examples:
    # Compare two models using UUIDs
    python compare_models.py compare abc123-def456 xyz789-uvw012 --rounds 50 --public-id YOUR_ID --secret-key YOUR_KEY

    # Compare using model names (your own models)
    python compare_models.py compare "my_model" "another_model" --rounds 50 --public-id YOUR_ID --secret-key YOUR_KEY

    # Mix model names and UUIDs
    python compare_models.py compare "my_model_t8" abc123-def456 --rounds 50

    # Get your models list
    python compare_models.py get-models --public-id YOUR_ID --secret-key YOUR_KEY

    # With environment variables set:
    python compare_models.py compare "my_model" "another_model" --rounds 50
    python compare_models.py get-models
"""

import json
import polars as pl
from typing import Dict, List, Optional, Annotated
import sys
import os
import re
from datetime import datetime
import typer
from enum import Enum
from tabulate import tabulate

from numerai_client import NumeraiGraphQLClient, Tournament, get_user_models




def get_model_performance(client: NumeraiGraphQLClient, model_id: str,
                         tournament: int = 8, last_n_rounds: int = 20) -> List[Dict]:
    """Get performance data for a specific model"""

    query = """
    query GetModelPerformance($modelId: String!, $tournament: Int!) {
        v2RoundModelPerformances(
            modelId: $modelId,
            tournament: $tournament
        ) {
            roundNumber
            roundResolved
            submissionScores {
                displayName
                value
                percentile
            }
        }
    }
    """

    variables = {
        "modelId": model_id,
        "tournament": tournament
    }

    result = client.query(query, variables)

    # Debug: print the raw result to understand what we're getting
    if not result:
        print(f"No data returned for model {model_id}", file=sys.stderr)
        return []

    performances = result.get("v2RoundModelPerformances", [])
    print(f"Found {len(performances)} performance records for model {model_id}", file=sys.stderr)


    # Sort by round number descending and take the last N (both resolved and unresolved)
    performances.sort(key=lambda x: x.get("roundNumber", 0), reverse=True)
    limited_performances = performances[:last_n_rounds]

    resolved_count = sum(1 for p in limited_performances if p.get("roundResolved"))
    print(f"Found {len(limited_performances)} rounds total ({resolved_count} resolved) for model {model_id}", file=sys.stderr)

    return limited_performances


def get_model_info(client: NumeraiGraphQLClient, model_id: str) -> Dict:
    """Get basic model information"""

    query = """
    query GetModelInfo($modelId: ID!) {
        model(modelId: $modelId) {
            id
            name
            username
            tournament
        }
    }
    """

    variables = {"modelId": model_id}
    result = client.query(query, variables)
    return result.get("model", {})




def is_valid_uuid(uuid_string: str) -> bool:
    """Check if a string is a valid UUID format"""
    uuid_pattern = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        re.IGNORECASE
    )
    return bool(uuid_pattern.match(uuid_string))


def resolve_model_identifier(client: NumeraiGraphQLClient, model_identifier: str) -> str:
    """
    Resolve a model identifier to a UUID.
    If it's already a UUID, return it as-is.
    If it's a model name, look up the UUID from user's models.
    """
    # Check if it's already a valid UUID
    if is_valid_uuid(model_identifier):
        return model_identifier

    # It's a model name, so fetch user models and look it up
    typer.echo(f"Looking up UUID for model name: {model_identifier}", err=True)
    user_models_list = get_user_models(client)

    if not user_models_list:
        typer.echo("Error: Could not fetch user models for name lookup.", err=True)
        raise typer.Exit(1)

    # Create mapping from model names to UUIDs for lookup
    user_models = {}
    for model in user_models_list:
        model_id = model.get("id")
        model_name = model.get("name")
        tournament = model.get("tournament")

        if model_id and model_name:
            # Include tournament info in the key for clarity
            key = f"{model_name}"
            if tournament:
                key = f"{model_name}_t{tournament}"
            user_models[key] = model_id
            # Also add without tournament suffix for convenience
            user_models[model_name] = model_id

    # Look for exact match first
    if model_identifier in user_models:
        uuid = user_models[model_identifier]
        typer.echo(f"Found exact match: {model_identifier} -> {uuid}", err=True)
        return uuid

    # Look for partial matches (case-insensitive)
    matches = []
    for model_name, uuid in user_models.items():
        if model_identifier.lower() in model_name.lower():
            matches.append((model_name, uuid))

    if len(matches) == 1:
        model_name, uuid = matches[0]
        typer.echo(f"Found partial match: {model_identifier} -> {model_name} -> {uuid}", err=True)
        return uuid
    elif len(matches) > 1:
        typer.echo(f"Error: Multiple models found matching '{model_identifier}':", err=True)
        for model_name, uuid in matches:
            typer.echo(f"  - {model_name}: {uuid}", err=True)
        typer.echo("Please use a more specific model name or the exact UUID.", err=True)
        raise typer.Exit(1)
    else:
        typer.echo(f"Error: No model found matching '{model_identifier}'.", err=True)
        typer.echo("Available models:", err=True)
        for model_name, uuid in user_models.items():
            typer.echo(f"  - {model_name}: {uuid}", err=True)
        raise typer.Exit(1)


def get_round_dates(client: NumeraiGraphQLClient, tournament: int = 8,
                   round_numbers: List[int] = None) -> Dict[int, str]:
    """Get round dates for the given round numbers"""

    query = """
    query GetRoundDates($tournament: Int!) {
        rounds(tournament: $tournament, limit: 200) {
            number
            openTime
            closeTime
            resolveTime
        }
    }
    """

    variables = {"tournament": tournament}
    result = client.query(query, variables)
    rounds_data = result.get("rounds", [])

    round_dates = {}
    for round_data in rounds_data:
        round_num = round_data.get("number")
        resolve_time = round_data.get("resolveTime")
        if round_num and resolve_time:
            round_dates[round_num] = resolve_time

    return round_dates


def compare_models(model_a_data: List[Dict], model_b_data: List[Dict],
                  model_a_name: str, model_b_name: str) -> pl.DataFrame:
    """Compare two models' performance data across multiple metrics"""

    def extract_all_metrics(data: List[Dict]) -> pl.DataFrame:
        """Extract all relevant metrics from the submission scores format"""
        rows = []
        for round_data in data:
            round_num = round_data.get("roundNumber")
            round_resolved = round_data.get("roundResolved", False)
            submission_scores = round_data.get("submissionScores", [])

            round_metrics = {
                "roundNumber": round_num,
                "resolved": round_resolved,
                "v2_corr20": None,
                "canon_mmc": None
            }

            for score in submission_scores:
                display_name = score.get("displayName", "")
                if display_name in ["v2_corr20", "canon_mmc"]:
                    round_metrics[display_name] = score.get("value")

            if round_num is not None:
                rows.append(round_metrics)

        return pl.DataFrame(rows)

    df_a = extract_all_metrics(model_a_data)
    df_b = extract_all_metrics(model_b_data)

    if df_a.is_empty() or df_b.is_empty():
        return pl.DataFrame()

    # Rename overlapping columns with suffixes before join
    overlap_cols = ["resolved", "v2_corr20", "canon_mmc"]
    df_a = df_a.rename({col: f"{col}_a" for col in overlap_cols})
    df_b = df_b.rename({col: f"{col}_b" for col in overlap_cols})
    merged = df_a.join(df_b, on="roundNumber", how="inner")

    # Use resolved status from either model (should be the same)
    merged = merged.with_columns(pl.col("resolved_a").alias("resolved"))

    # Calculate differences (polars handles null subtraction natively)
    for metric in ["v2_corr20", "canon_mmc"]:
        merged = merged.with_columns(
            (pl.col(f"{metric}_a") - pl.col(f"{metric}_b")).alias(f"{metric}_diff")
        )

    # Rename columns for clarity using actual model names
    clean_model_a = model_a_name.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
    clean_model_b = model_b_name.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")

    column_renames = {"roundNumber": "Round"}
    for metric in ["v2_corr20", "canon_mmc"]:
        column_renames[f"{metric}_a"] = f"{metric}_{clean_model_a}"
        column_renames[f"{metric}_b"] = f"{metric}_{clean_model_b}"

    merged = merged.rename(column_renames)

    columns = ["Round", "resolved",
               f"v2_corr20_{clean_model_a}", f"v2_corr20_{clean_model_b}", "v2_corr20_diff",
               f"canon_mmc_{clean_model_a}", f"canon_mmc_{clean_model_b}", "canon_mmc_diff"]

    return merged.select(columns)


def format_table(df: pl.DataFrame, round_dates: Dict[int, str]) -> str:
    """Format the comparison table with dates and multiple metrics"""

    if df.is_empty():
        return "No overlapping data found between the two models."

    # Add date and resolution columns
    df = df.with_columns(
        pl.col("Round").map_elements(lambda x: round_dates.get(x, "Unknown"), return_dtype=pl.Utf8).alias("Date"),
        pl.when(pl.col("resolved")).then(pl.lit("Resolved")).otherwise(pl.lit("Unresolved")).alias("Resolution_Status"),
    )

    # Parse dates for sorting
    df = df.with_columns(pl.col("Date").str.to_datetime(strict=False).alias("date_parsed"))
    df = df.sort("date_parsed", descending=True)

    # Select display columns
    metric_columns = [col for col in df.columns if any(metric in col for metric in ["v2_corr20", "canon_mmc"])]
    columns = ["Round", "Date", "Resolution_Status"] + metric_columns
    df = df.select(columns)

    # Format rows for display
    rows = []
    for row in df.iter_rows(named=True):
        formatted = []
        for col in columns:
            val = row[col]
            if col in ("Round", "Date", "Resolution_Status"):
                formatted.append(val)
            elif val is None:
                formatted.append("N/A")
            else:
                formatted.append(f"{val:.6f}")
        rows.append(formatted)

    return tabulate(rows, headers=columns, tablefmt="plain")


class MetricType(str, Enum):
    """Available performance metrics for comparison"""
    corr = "corr"
    mmc = "mmc"
    fnc = "fnc"
    tc = "tc"


class OutputFormat(str, Enum):
    """Available output formats"""
    json = "json"
    table = "table"


app = typer.Typer(help="Compare two Numerai models' historical performance")


@app.command()
def compare(
    model_a: Annotated[str, typer.Argument(help="Model A identifier (UUID or model name)")],
    model_b: Annotated[str, typer.Argument(help="Model B identifier (UUID or model name)")],
    metric: Annotated[MetricType, typer.Option(help="Performance metric to compare")] = MetricType.corr,
    rounds: Annotated[int, typer.Option(help="Number of recent rounds to fetch")] = 20,
    tournament: Annotated[int, typer.Option(help="Tournament ID (8=classic, 11=signals, 12=crypto)")] = 8,
    output_csv: Annotated[Optional[str], typer.Option("--output", "-o", help="Output CSV file path (optional)")] = None,
    public_id: Annotated[Optional[str], typer.Option(help="Numerai public API ID (or set NUMER_PUBLIC_API_KEY env var)")] = None,
    secret_key: Annotated[Optional[str], typer.Option(help="Numerai secret API key (or set NUMER_SECRET_API_KEY env var)")] = None,
):
    """
    Compare the historical resolved round performance data between two Numerai models
    and output a table showing the differences ordered by date (most recent first).

    Model identifiers can be either UUIDs or model names. If using model names,
    they must belong to your authenticated account.

    Examples with UUIDs:
        python compare_models.py compare abc123-def456 xyz789-uvw012 --rounds 50

    Examples with model names:
        python compare_models.py compare "my_model" "another_model" --rounds 50
        python compare_models.py compare "my_model_t8" xyz789-uvw012 --rounds 50

    Export to CSV:
        python compare_models.py compare "my_model" "another_model" --rounds 50 --output results.csv

    Authentication can be provided via command line options or environment variables:
        python compare_models.py compare "my_model" "another_model" --public-id YOUR_ID --secret-key YOUR_KEY

    Or set environment variables:
        export NUMER_PUBLIC_API_KEY=your_public_id
        export NUMER_SECRET_API_KEY=your_secret_key
    """
    # Get authentication from CLI args or environment variables
    api_public_id = public_id or os.environ.get("NUMER_PUBLIC_API_KEY")
    api_secret_key = secret_key or os.environ.get("NUMER_SECRET_API_KEY")

    if not api_public_id or not api_secret_key:
        typer.echo("Error: Authentication required. Provide --public-id and --secret-key or set environment variables:", err=True)
        typer.echo("  NUMER_PUBLIC_API_KEY=your_public_id", err=True)
        typer.echo("  NUMER_SECRET_API_KEY=your_secret_key", err=True)
        typer.echo("\nGet your API keys from: https://numer.ai/account", err=True)
        raise typer.Exit(1)

    with NumeraiGraphQLClient(public_id=api_public_id, secret_key=api_secret_key) as client:
        # Resolve model identifiers to UUIDs
        typer.echo("Resolving model identifiers...")
        model_a_uuid = resolve_model_identifier(client, model_a)
        model_b_uuid = resolve_model_identifier(client, model_b)

        typer.echo("Fetching model information...")

        # Try to get model info, but continue even if it fails due to permissions
        model_a_info = get_model_info(client, model_a_uuid)
        model_b_info = get_model_info(client, model_b_uuid)

        # Use model IDs as names if we can't get the actual names
        model_a_name = f"{model_a_info.get('name', 'Model A')} ({model_a_info.get('username', 'Unknown')})" if model_a_info else f"Model A ({model_a_uuid[:8]}...)"
        model_b_name = f"{model_b_info.get('name', 'Model B')} ({model_b_info.get('username', 'Unknown')})" if model_b_info else f"Model B ({model_b_uuid[:8]}...)"

        typer.echo("Comparing models:")
        typer.echo(f"  Model A: {model_a_name}")
        typer.echo(f"  Model B: {model_b_name}")
        typer.echo(f"  Metrics: v2_corr20, canon_mmc")
        typer.echo(f"  Rounds: {rounds}")
        typer.echo()

        # Get performance data
        typer.echo("Fetching performance data...")
        model_a_data = get_model_performance(client, model_a_uuid, tournament, rounds)
        model_b_data = get_model_performance(client, model_b_uuid, tournament, rounds)

        if not model_a_data or not model_b_data:
            typer.echo("Error: Could not fetch performance data for one or both models.", err=True)
            raise typer.Exit(1)

        # Compare models
        comparison_df = compare_models(model_a_data, model_b_data, model_a_name, model_b_name)

        if comparison_df.is_empty():
            typer.echo("No overlapping rounds found between the two models.")
            raise typer.Exit(0)

        # Get round dates
        typer.echo("Fetching round dates...")
        round_numbers = comparison_df["Round"].to_list()
        round_dates = get_round_dates(client, tournament, round_numbers)

    # Format and display results
    typer.echo("\nModel Comparison Results:")
    typer.echo("=" * 80)
    table = format_table(comparison_df, round_dates)
    typer.echo(table)

    # Export to CSV if requested
    if output_csv:
        try:
            if not comparison_df.is_empty():
                # Add date and resolution status columns for CSV
                export_df = comparison_df.with_columns(
                    pl.col("Round").map_elements(lambda x: round_dates.get(x, "Unknown"), return_dtype=pl.Utf8).alias("Date"),
                    pl.when(pl.col("resolved")).then(pl.lit("Resolved")).otherwise(pl.lit("Unresolved")).alias("Resolution_Status"),
                )
                export_df = export_df.with_columns(
                    pl.col("Date").str.to_datetime(strict=False).alias("date_parsed")
                )
                export_df = export_df.sort("date_parsed", descending=True)

                metric_columns = [col for col in export_df.columns if any(metric in col for metric in ["v2_corr20", "canon_mmc"])]
                csv_columns = ["Round", "Date", "Resolution_Status"] + metric_columns

                export_df.select(csv_columns).write_csv(output_csv, float_precision=6)
                typer.echo(f"\nResults exported to: {output_csv}")
            else:
                typer.echo(f"\nNo rounds to export to CSV.", err=True)
        except Exception as e:
            typer.echo(f"\nError exporting to CSV: {e}", err=True)

    # Summary statistics for both resolved and unresolved rounds
    resolved_df = comparison_df.filter(pl.col("resolved"))
    unresolved_df = comparison_df.filter(~pl.col("resolved"))

    typer.echo("\nSummary Statistics:")
    typer.echo(f"  Total overlapping rounds: {len(comparison_df)}")
    typer.echo(f"  Resolved rounds: {len(resolved_df)}")
    typer.echo(f"  Unresolved rounds: {len(unresolved_df)}")

    clean_model_a = model_a_name.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
    clean_model_b = model_b_name.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")

    def _print_metric_stats(subset_df: pl.DataFrame, section_label: str) -> None:
        if len(subset_df) == 0:
            typer.echo(f"\n--- {section_label} ---")
            typer.echo("  No rounds with data found." if "RESOLVED" in section_label and "UN" not in section_label
                       else "  No unresolved rounds found.")
            return

        typer.echo(f"\n--- {section_label} ---")
        for metric in ["v2_corr20", "canon_mmc"]:
            diff_col = f"{metric}_diff"
            model_a_col = f"{metric}_{clean_model_a}"
            model_b_col = f"{metric}_{clean_model_b}"

            if diff_col not in subset_df.columns:
                continue
            valid_diffs = subset_df[diff_col].drop_nulls()
            if len(valid_diffs) == 0:
                typer.echo(f"\n  {metric.upper()}: No data available (metrics not yet calculated)")
                continue

            model_a_scores = subset_df[model_a_col].drop_nulls() if model_a_col in subset_df.columns else pl.Series([])
            model_b_scores = subset_df[model_b_col].drop_nulls() if model_b_col in subset_df.columns else pl.Series([])

            typer.echo(f"\n  {metric.upper()}:")
            typer.echo(f"    Average difference ({model_a_name} - {model_b_name}): {valid_diffs.mean():.6f}")
            typer.echo(f"    Standard deviation: {valid_diffs.std():.6f}")
            typer.echo(f"    {model_a_name} wins: {(valid_diffs > 0).sum()} rounds")
            typer.echo(f"    {model_b_name} wins: {(valid_diffs < 0).sum()} rounds")
            typer.echo(f"    Ties: {(valid_diffs == 0).sum()} rounds")

            if len(model_a_scores) > 0:
                typer.echo(f"    Total {model_a_name} score: {model_a_scores.sum():.6f}")
            if len(model_b_scores) > 0:
                typer.echo(f"    Total {model_b_name} score: {model_b_scores.sum():.6f}")
            if len(model_a_scores) > 0 and len(model_b_scores) > 0:
                total_diff = model_a_scores.sum() - model_b_scores.sum()
                typer.echo(f"    Total difference ({model_a_name} - {model_b_name}): {total_diff:.6f}")

    _print_metric_stats(resolved_df, "RESOLVED ROUNDS STATISTICS")
    _print_metric_stats(unresolved_df, "UNRESOLVED ROUNDS STATISTICS")


@app.command()
def get_models(
    public_id: Annotated[Optional[str], typer.Option(help="Numerai public API ID (or set NUMER_PUBLIC_API_KEY env var)")] = None,
    secret_key: Annotated[Optional[str], typer.Option(help="Numerai secret API key (or set NUMER_SECRET_API_KEY env var)")] = None,
):
    """
    Get all models for the authenticated user and output as JSON mapping.

    Example:
        python compare_models.py get-models --public-id YOUR_ID --secret-key YOUR_KEY

    Or with environment variables:
        export NUMER_PUBLIC_API_KEY=your_public_id
        export NUMER_SECRET_API_KEY=your_secret_key
        python compare_models.py get-models
    """
    # Get authentication from CLI args or environment variables
    api_public_id = public_id or os.environ.get("NUMER_PUBLIC_API_KEY")
    api_secret_key = secret_key or os.environ.get("NUMER_SECRET_API_KEY")

    if not api_public_id or not api_secret_key:
        typer.echo("Error: Authentication required. Provide --public-id and --secret-key or set environment variables:", err=True)
        typer.echo("  NUMER_PUBLIC_API_KEY=your_public_id", err=True)
        typer.echo("  NUMER_SECRET_API_KEY=your_secret_key", err=True)
        typer.echo("\nGet your API keys from: https://numer.ai/account", err=True)
        raise typer.Exit(1)

    with NumeraiGraphQLClient(public_id=api_public_id, secret_key=api_secret_key) as client:
        typer.echo("Fetching user models...", err=True)

        models_list = get_user_models(client)

    if not models_list:
        typer.echo("No models found or authentication failed.", err=True)
        raise typer.Exit(1)

    # Create mapping from model names to UUIDs for JSON output
    models = {}
    for model in models_list:
        model_id = model.get("id")
        model_name = model.get("name")
        tournament = model.get("tournament")

        if model_id and model_name:
            # Include tournament info in the key for clarity
            key = f"{model_name}"
            if tournament:
                key = f"{model_name}_t{tournament}"
            models[key] = model_id

    # Output JSON to stdout
    print(json.dumps(models, indent=2))


def get_top_accounts(client: NumeraiGraphQLClient, limit: int = 10, tournament: int = 8) -> List[Dict]:
    """Get top accounts from leaderboard ordered by MMC"""

    query = """
    query GetTopAccounts($tournament: Int!, $limit: Int!) {
        accountLeaderboard(
            tournament: $tournament,
            limit: $limit,
            orderBy: "mmc",
            direction: "desc"
        ) {
            username
            displayName
            rank
            mmc
            nmrStaked
            corr
        }
    }
    """

    variables = {
        "tournament": tournament,
        "limit": limit
    }

    result = client.query(query, variables)
    return result.get("accountLeaderboard", [])


def get_account_best_model(client: NumeraiGraphQLClient, username: str, tournament: int = 8) -> Dict:
    """Get the best model for a user (highest staked or best performing)"""

    query = """
    query GetAccountProfile($username: String!, $tournament: Int!) {
        accountProfile(username: $username, tournament: $tournament) {
            models {
                id
                tournament
            }
        }
    }
    """

    variables = {
        "username": username,
        "tournament": tournament
    }

    result = client.query(query, variables)
    account_data = result.get("accountProfile", {})
    models = account_data.get("models", [])

    if not models:
        return {}

    # Filter models for the correct tournament
    tournament_models = [m for m in models if m.get("tournament") == tournament]

    if not tournament_models:
        return {}

    # Just return the first model found for the tournament
    # In a future enhancement, we could query individual model details for stake info
    return tournament_models[0]


def format_top_models_output(top_data: List[Dict], output_format: OutputFormat) -> str:
    """Format top models data for output"""

    if output_format == OutputFormat.json:
        return json.dumps(top_data, indent=2)

    # Table format
    if not top_data:
        return "No data found."

    headers = ["Rank", "Username", "Display Name", "MMC", "Correlation", "NMR Staked", "Best Model", "Model ID"]
    rows = []

    for item in top_data:
        rows.append([
            item.get("rank", "N/A"),
            item.get("username", "N/A"),
            item.get("displayName", "N/A"),
            f"{item.get('mmc', 0):.6f}" if item.get("mmc") is not None else "N/A",
            f"{item.get('corr', 0):.6f}" if item.get("corr") is not None else "N/A",
            f"{float(item.get('nmrStaked', 0)):.2f}" if item.get("nmrStaked") is not None else "N/A",
            item.get("best_model_name", "N/A"),
            item.get("best_model_id", "N/A")[:8] + "..." if item.get("best_model_id") else "N/A"
        ])

    return tabulate(rows, headers=headers, tablefmt="grid")


@app.command()
def top(
    limit: Annotated[int, typer.Option(help="Number of top models to return")] = 10,
    tournament: Annotated[int, typer.Option(help="Tournament ID (8=classic, 11=signals, 12=crypto)")] = 8,
    output_format: Annotated[OutputFormat, typer.Option("--format", "-f", help="Output format")] = OutputFormat.table,
    public_id: Annotated[Optional[str], typer.Option(help="Numerai public API ID (optional, will try without auth first)")] = None,
    secret_key: Annotated[Optional[str], typer.Option(help="Numerai secret API key (optional, will try without auth first)")] = None,
):
    """
    Get the top models ordered by MMC score.

    This command fetches the top accounts from the leaderboard and then finds
    the best model for each account (highest staked or best performing).

    Examples:
        # Get top 10 models in table format
        python compare_models.py top

        # Get top 20 models in JSON format
        python compare_models.py top --limit 20 --format json

        # Get top 5 models for Signals tournament
        python compare_models.py top --limit 5 --tournament 11
    """
    # Try without authentication first
    with NumeraiGraphQLClient() as client:
        typer.echo(f"Fetching top {limit} accounts by MMC from tournament {tournament}...", err=True)

        top_accounts = get_top_accounts(client, limit, tournament)

        if not top_accounts:
            # Try with authentication if available
            api_public_id = public_id or os.environ.get("NUMER_PUBLIC_API_KEY")
            api_secret_key = secret_key or os.environ.get("NUMER_SECRET_API_KEY")

            if api_public_id and api_secret_key:
                typer.echo("Retrying with authentication...", err=True)
                with NumeraiGraphQLClient(public_id=api_public_id, secret_key=api_secret_key) as auth_client:
                    top_accounts = get_top_accounts(auth_client, limit, tournament)

            if not top_accounts:
                typer.echo("Error: Could not fetch top accounts data.", err=True)
                raise typer.Exit(1)

        typer.echo(f"Found {len(top_accounts)} accounts. Fetching best models...", err=True)

        # Get best model for each account
        top_models_data = []
        for account in top_accounts:
            username = account.get("username")
            if not username:
                continue

            best_model = get_account_best_model(client, username, tournament)

            # Combine account data with model data
            model_data = {
                "rank": account.get("rank"),
                "username": username,
                "displayName": account.get("displayName"),
                "mmc": account.get("mmc"),
                "corr": account.get("corr"),
                "nmrStaked": account.get("nmrStaked"),
                "best_model_name": f"Model for {username}" if best_model.get("id") else "No model found",
                "best_model_id": best_model.get("id", "")
            }

            top_models_data.append(model_data)

    # Output results
    output = format_top_models_output(top_models_data, output_format)
    print(output)


def read_compare_script(script_path: str = "compare_all.sh") -> List[str]:
    """Read existing compare_all.sh script and return lines"""
    try:
        with open(script_path, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return ["#!/bin/bash\n\n"]


def parse_compare_entries(lines: List[str]) -> Dict[str, Dict]:
    """Parse existing comparison entries from script lines"""
    entries = {}

    for line in lines:
        line = line.strip()
        if line.startswith('uv run compare_models.py compare'):
            # Parse the command line
            # Example: uv run compare_models.py compare --output "t1_shatteredx.csv" --rounds 200 fnc_imp_01 e17ad85c-b2ed-44f9-9240-71d54e01fcc4

            # Extract output filename to get username
            output_match = re.search(r'--output "t1_([^.]+)\.csv"', line)
            if output_match:
                username = output_match.group(1)

                # Extract other parameters
                rounds_match = re.search(r'--rounds (\d+)', line)
                rounds = int(rounds_match.group(1)) if rounds_match else 200

                # Extract baseline and target model IDs (last two arguments)
                parts = line.split()
                if len(parts) >= 2:
                    target_model_id = parts[-1]
                    baseline_model_id = parts[-2]

                    entries[username] = {
                        'baseline_model': baseline_model_id,
                        'target_model': target_model_id,
                        'rounds': rounds,
                        'output_file': f't1_{username}.csv'
                    }

    return entries


def generate_compare_command(username: str, baseline_model: str, target_model: str, rounds: int) -> str:
    """Generate a single comparison command"""
    output_file = f"t1_{username}.csv"
    return f'uv run compare_models.py compare --output "{output_file}" --rounds {rounds} {baseline_model} {target_model}'


def smart_merge_entries(existing_entries: Dict[str, Dict], new_top_data: List[Dict],
                       baseline_model: str, rounds: int) -> Dict[str, Dict]:
    """Smart merge existing entries with new top user data"""
    merged = existing_entries.copy()

    for item in new_top_data:
        username = item.get('username')
        model_id = item.get('best_model_id')

        if username and model_id:
            # Update or add entry
            merged[username] = {
                'baseline_model': baseline_model,
                'target_model': model_id,
                'rounds': rounds,
                'output_file': f't1_{username}.csv'
            }

    return merged


def write_compare_script(entries: Dict[str, Dict], script_path: str = "compare_all.sh"):
    """Write the updated compare script"""
    lines = ["#!/bin/bash\n", "\n"]

    # Sort entries by username for consistent output
    for username in sorted(entries.keys()):
        entry = entries[username]
        command = generate_compare_command(
            username,
            entry['baseline_model'],
            entry['target_model'],
            entry['rounds']
        )
        lines.append(command + "\n")

    lines.append("\n\n\n\n")

    with open(script_path, 'w') as f:
        f.writelines(lines)


@app.command()
def top_compare(
    limit: Annotated[int, typer.Option(help="Number of top models to include")] = 10,
    tournament: Annotated[int, typer.Option(help="Tournament ID (8=classic, 11=signals, 12=crypto)")] = 8,
    baseline_model: Annotated[str, typer.Option(help="Baseline model ID to compare against")] = "fnc_imp_01",
    rounds: Annotated[int, typer.Option(help="Number of rounds to compare")] = 200,
    script_path: Annotated[str, typer.Option(help="Path to compare script file")] = "compare_all.sh",
    public_id: Annotated[Optional[str], typer.Option(help="Numerai public API ID (optional)")] = None,
    secret_key: Annotated[Optional[str], typer.Option(help="Numerai secret API key (optional)")] = None,
):
    """
    Generate or update compare_all.sh script with top models comparisons.

    This command fetches the top models and creates/updates a shell script
    with comparison commands for each top user's best model against a baseline.
    Uses smart merging to preserve existing entries while adding/updating top users.

    Examples:
        # Generate script with top 10 models vs fnc_imp_01
        python compare_models.py top-compare

        # Top 5 models vs custom baseline with 500 rounds
        python compare_models.py top-compare --limit 5 --baseline-model my_model_id --rounds 500

        # Update script for Signals tournament
        python compare_models.py top-compare --tournament 11
    """

    # Get top models data using existing functionality
    typer.echo(f"Fetching top {limit} models from tournament {tournament}...", err=True)

    # Try without authentication first
    with NumeraiGraphQLClient() as client:
        top_accounts = get_top_accounts(client, limit, tournament)

        if not top_accounts:
            # Try with authentication if available
            api_public_id = public_id or os.environ.get("NUMER_PUBLIC_API_KEY")
            api_secret_key = secret_key or os.environ.get("NUMER_SECRET_API_KEY")

            if api_public_id and api_secret_key:
                typer.echo("Retrying with authentication...", err=True)
                with NumeraiGraphQLClient(public_id=api_public_id, secret_key=api_secret_key) as auth_client:
                    top_accounts = get_top_accounts(auth_client, limit, tournament)

            if not top_accounts:
                typer.echo("Error: Could not fetch top accounts data.", err=True)
                raise typer.Exit(1)

        # Get best models for each account
        typer.echo(f"Found {len(top_accounts)} accounts. Fetching best models...", err=True)

        top_models_data = []
        for account in top_accounts:
            username = account.get("username")
            if not username:
                continue

            best_model = get_account_best_model(client, username, tournament)

            if best_model.get("id"):
                model_data = {
                    "username": username,
                    "best_model_id": best_model.get("id")
                }
                top_models_data.append(model_data)

    if not top_models_data:
        typer.echo("Error: No models found for top accounts.", err=True)
        raise typer.Exit(1)

    # Read existing script
    typer.echo(f"Reading existing script: {script_path}", err=True)
    existing_lines = read_compare_script(script_path)
    existing_entries = parse_compare_entries(existing_lines)

    # Smart merge
    typer.echo(f"Merging {len(existing_entries)} existing entries with {len(top_models_data)} new entries...", err=True)
    merged_entries = smart_merge_entries(existing_entries, top_models_data, baseline_model, rounds)

    # Write updated script
    write_compare_script(merged_entries, script_path)

    typer.echo(f"\nUpdated {script_path} with {len(merged_entries)} comparison entries:", err=True)
    for username in sorted(merged_entries.keys()):
        entry = merged_entries[username]
        typer.echo(f"  {username}: {entry['baseline_model']} vs {entry['target_model'][:8]}...", err=True)

    typer.echo(f"\nRun the script with: bash {script_path}", err=True)


if __name__ == "__main__":
    app()