#!/usr/bin/env python3
"""
Numerai Model Listing Tool

This script lists model names and their corresponding model IDs from the Numerai API.
Supports both authenticated (your own models) and anonymous (public models) access.

Usage:
    python list_models.py [--username USERNAME] [--tournament {8,11,12}] [--format {csv,json,table}] [--public-id PUBLIC_ID] [--secret-key SECRET_KEY]

Authentication:
    If --public-id and --secret-key are provided or NUMER_PUBLIC_API_KEY and NUMER_SECRET_API_KEY
    environment variables are set, the script will fetch your own models.

    If --username is provided, it will fetch public models for that user (no auth required).

    If no auth and no username, it will show a warning and exit.

Examples:
    # List your own models (requires auth)
    python list_models.py --public-id YOUR_ID --secret-key YOUR_KEY

    # List public models for a specific user
    python list_models.py --username some_user

    # List models in JSON format for signals tournament
    python list_models.py --username some_user --tournament 11 --format json

    # With environment variables set
    export NUMER_PUBLIC_API_KEY=your_public_id
    export NUMER_SECRET_API_KEY=your_secret_key
    python list_models.py --tournament 8 --format table
"""

import os
import sys
import csv
import json
from io import StringIO
from typing import List, Dict, Optional, Annotated
import typer
from enum import Enum
from tabulate import tabulate

from numerai_client import NumeraiGraphQLClient, Tournament, get_tournaments_info, get_user_models, get_account_models, get_all_models_for_all_users


class OutputFormat(str, Enum):
    """Available output formats"""
    CSV = "csv"
    JSON = "json"
    TABLE = "table"


app = typer.Typer(help="List Numerai model names and IDs")


def format_models_output(models: List[Dict], output_format: OutputFormat, include_username: bool = False) -> str:
    """Format models data for output"""

    if not models:
        return "No models found."

    if output_format == OutputFormat.JSON:
        # Create a clean mapping for JSON output
        if include_username:
            model_mapping = {
                f"{model.get('username', 'unknown')}:{model['name']}": model["id"]
                for model in models
            }
        else:
            model_mapping = {
                model["name"]: model["id"]
                for model in models
            }
        return json.dumps(model_mapping, indent=2)

    elif output_format == OutputFormat.CSV:
        # Create CSV output
        output = StringIO()
        writer = csv.writer(output)

        if include_username:
            writer.writerow(["username", "model_name", "model_id", "tournament"])
            for model in models:
                writer.writerow([
                    model.get("username", ""),
                    model["name"],
                    model["id"],
                    model.get("tournament", "")
                ])
        else:
            writer.writerow(["model_name", "model_id", "tournament"])
            for model in models:
                writer.writerow([
                    model["name"],
                    model["id"],
                    model.get("tournament", "")
                ])

        return output.getvalue().strip()

    elif output_format == OutputFormat.TABLE:
        # Create table output
        if include_username:
            headers = ["Username", "Model Name", "Model ID", "Tournament"]
            rows = []
            for model in models:
                tournament_name = get_tournaments_info().get(model.get("tournament"), f"T{model.get('tournament', '')}")
                rows.append([
                    model.get("username", ""),
                    model["name"],
                    model["id"],
                    tournament_name
                ])
        else:
            headers = ["Model Name", "Model ID", "Tournament"]
            rows = []
            for model in models:
                tournament_name = get_tournaments_info().get(model.get("tournament"), f"T{model.get('tournament', '')}")
                rows.append([
                    model["name"],
                    model["id"],
                    tournament_name
                ])

        return tabulate(rows, headers=headers, tablefmt="grid")

    return "Invalid output format"


def write_output_to_file(content: str, filepath: str) -> None:
    """Write output content to a file"""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        typer.echo(f"Results written to: {filepath}", err=True)
    except Exception as e:
        typer.echo(f"Error writing to file {filepath}: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def main(
    username: Optional[str] = typer.Option(None, help="Username to fetch public models for"),
    all_users: bool = typer.Option(False, "--all-users", help="Fetch models for ALL users (WARNING: This is a large operation)"),
    user_limit: int = typer.Option(1000, help="Maximum number of users to process when using --all-users"),
    request_delay: float = typer.Option(0.5, help="Delay between requests in seconds (for --all-users mode to avoid rate limiting)"),
    save_frequency: int = typer.Option(1, help="Save to file every N users when using --all-users with --output-file (default: 1)"),
    tournament: Optional[Tournament] = typer.Option(None, help="Tournament to filter by (8=classic, 11=signals, 12=crypto)"),
    output_format: OutputFormat = typer.Option(OutputFormat.CSV, "--format", "-f", help="Output format"),
    output_file: Optional[str] = typer.Option(None, "--output-file", "-o", help="Write results to file instead of stdout"),
    public_id: Optional[str] = typer.Option(None, help="Numerai public API ID (or set NUMER_PUBLIC_API_KEY env var)"),
    secret_key: Optional[str] = typer.Option(None, help="Numerai secret API key (or set NUMER_SECRET_API_KEY env var)"),
):
    """
    List Numerai model names and their corresponding model IDs.

    This command can work in multiple modes:
    1. Authenticated mode: Get your own models (requires API keys)
    2. Public mode: Get public models for a specific username
    3. All users mode: Get models for ALL users (WARNING: Large operation)

    Tournament options:
        8  = Classic Numerai Tournament
        11 = Numerai Signals
        12 = Crypto Signals

    Examples:
        # List your own models in CSV format
        python list_models.py --public-id YOUR_ID --secret-key YOUR_KEY

        # List public models for a user in JSON format
        python list_models.py --username integration_test --format json

        # Filter by tournament and output as table
        python list_models.py --username some_user --tournament 8 --format table

        # Get ALL users' models (WARNING: Large operation, use with --output-file)
        python list_models.py --all-users --user-limit 500 --output-file all_models.csv

        # Slower requests to avoid rate limiting
        python list_models.py --all-users --request-delay 1.0 --output-file all_models.csv

        # Save every 10 users to reduce I/O overhead
        python list_models.py --all-users --save-frequency 10 --output-file all_models.csv

        # With environment variables
        export NUMER_PUBLIC_API_KEY=your_public_id
        export NUMER_SECRET_API_KEY=your_secret_key
        python list_models.py --format table
    """

    # Get authentication from CLI args or environment variables
    api_public_id = public_id or os.environ.get("NUMER_PUBLIC_API_KEY")
    api_secret_key = secret_key or os.environ.get("NUMER_SECRET_API_KEY")

    # Validate options
    if all_users and username:
        typer.echo("Error: Cannot use --all-users with --username. Choose one option.", err=True)
        raise typer.Exit(1)

    if all_users and (api_public_id or api_secret_key):
        typer.echo("Warning: --all-users mode doesn't use authentication. Remove auth options to avoid confusion.", err=True)

    # Check if incremental saving will be used (for output logic later)
    incremental_saving_used = False

    # Determine mode of operation
    if all_users:
        # All users mode - get models for ALL users
        typer.echo("WARNING: Fetching models for ALL users. This may take a very long time...", err=True)
        typer.echo(f"Processing up to {user_limit} users from tournament {tournament or Tournament.CLASSIC}...", err=True)

        if not output_file:
            typer.echo("RECOMMENDATION: Use --output-file to save results to a file instead of stdout.", err=True)

        with NumeraiGraphQLClient() as client:
            models = get_all_models_for_all_users(
                client,
                tournament,
                user_limit,
                request_delay,
                output_file,
                output_format.value,
                save_frequency
            )

        if not models:
            typer.echo("No models found.", err=True)
            raise typer.Exit(1)

        include_username = True  # Always include usernames for all-users mode

        # Update incremental saving flag
        incremental_saving_used = output_file and output_format.value.lower() in ['csv', 'json']

    elif api_public_id and api_secret_key:
        # Authenticated mode - get user's own models
        typer.echo("Using authenticated mode to fetch your models...", err=True)

        with NumeraiGraphQLClient(public_id=api_public_id, secret_key=api_secret_key) as client:
            models = get_user_models(client, tournament)

        if not models:
            typer.echo("No models found for your account.", err=True)
            if tournament:
                typer.echo(f"Try without tournament filter or check if you have models in tournament {tournament}.", err=True)
            raise typer.Exit(1)

        include_username = False

    elif username:
        # Public mode - get models for specified username
        typer.echo(f"Fetching public models for user: {username}...", err=True)

        with NumeraiGraphQLClient() as client:
            models = get_account_models(client, username, tournament)

        if not models:
            typer.echo(f"No public models found for user '{username}'.", err=True)
            if tournament:
                typer.echo(f"Try without tournament filter or check if the user has models in tournament {tournament}.", err=True)
            raise typer.Exit(1)

        include_username = False

    else:
        # No auth, username, or all-users provided
        typer.echo("ERROR: No operation mode specified.", err=True)
        typer.echo("", err=True)
        typer.echo("Choose one of the following modes:", err=True)
        typer.echo("", err=True)
        typer.echo("1. List your own models (requires authentication):", err=True)
        typer.echo("  --public-id YOUR_ID --secret-key YOUR_KEY", err=True)
        typer.echo("  OR set environment variables:", err=True)
        typer.echo("    export NUMER_PUBLIC_API_KEY=your_public_id", err=True)
        typer.echo("    export NUMER_SECRET_API_KEY=your_secret_key", err=True)
        typer.echo("", err=True)
        typer.echo("2. List public models for a specific user:", err=True)
        typer.echo("  --username some_username", err=True)
        typer.echo("", err=True)
        typer.echo("3. List models for ALL users (WARNING: Large operation):", err=True)
        typer.echo("  --all-users --user-limit 500 --output-file results.csv", err=True)
        typer.echo("", err=True)
        typer.echo("Get your API keys from: https://numer.ai/account", err=True)
        raise typer.Exit(1)

    # Skip regular output if incremental saving was used (data already saved)
    if not (all_users and incremental_saving_used):
        # Format the output
        output = format_models_output(models, output_format, include_username)

        # Write to file or print to stdout
        if output_file:
            write_output_to_file(output, output_file)
        else:
            print(output)

    # Show summary to stderr
    typer.echo(f"Found {len(models)} models", err=True)
    if tournament:
        tournament_name = get_tournaments_info().get(tournament, f"T{tournament}")
        typer.echo(f"Filtered by tournament: {tournament_name} ({tournament})", err=True)
    if all_users:
        typer.echo(f"Processed up to {user_limit} users", err=True)


if __name__ == "__main__":
    app()