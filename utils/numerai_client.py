#!/usr/bin/env python3
"""
Shared Numerai GraphQL Client

This module provides a reusable GraphQL client for interacting with the Numerai API.
Supports both authenticated and anonymous requests using httpx.
"""

import httpx
import json
import sys
import time
import random
import os
import csv
from typing import Dict, List, Optional, Set
from enum import Enum


class Tournament(int, Enum):
    """Available Numerai tournaments"""
    CLASSIC = 8
    SIGNALS = 11
    CRYPTO = 12


class NumeraiGraphQLClient:
    """Client for querying the Numerai GraphQL API"""

    def __init__(self, base_url: str = "https://api-tournament.numer.ai/",
                 public_id: Optional[str] = None, secret_key: Optional[str] = None):
        """
        Initialize the GraphQL client.

        Args:
            base_url: Numerai API endpoint
            public_id: Public API key for authentication
            secret_key: Secret API key for authentication
        """
        self.base_url = base_url
        self.client = httpx.Client()
        self.client.headers.update({"Content-Type": "application/json"})

        # Add authentication if provided
        if public_id and secret_key:
            self._add_auth_header(public_id, secret_key)

    def _add_auth_header(self, public_id: str, secret_key: str) -> None:
        """Add authentication header using public_id and secret_key"""
        # Numerai uses Token auth with public_id$secret_key format
        self.client.headers.update({"Authorization": f"Token {public_id}${secret_key}"})

    def _is_rate_limited(self, result: Dict) -> bool:
        """Check if the result indicates rate limiting"""
        if "errors" not in result:
            return False

        for error in result["errors"]:
            if error.get("code") == "rate_limited" or "rate limited" in error.get("message", "").lower():
                return True
        return False

    def query(self, query: str, variables: Optional[Dict] = None, max_retries: int = 5, initial_wait: float = 5.0) -> Dict:
        """
        Execute a GraphQL query with exponential backoff retry for rate limiting

        Args:
            query: GraphQL query string
            variables: Optional query variables
            max_retries: Maximum number of retry attempts
            initial_wait: Initial wait time in seconds

        Returns:
            GraphQL response data
        """
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        last_error = None

        for attempt in range(max_retries + 1):
            try:
                response = self.client.post(self.base_url, json=payload)
                response.raise_for_status()
                result = response.json()

                # Check for rate limiting in GraphQL errors
                if "errors" in result and self._is_rate_limited(result):
                    if attempt < max_retries:
                        # Calculate exponential backoff with jitter
                        wait_time = initial_wait * (2 ** attempt) + random.uniform(0, 1)
                        print(f"Rate limited. Retrying in {wait_time:.2f} seconds (attempt {attempt + 1}/{max_retries})...", file=sys.stderr)
                        time.sleep(wait_time)
                        continue
                    else:
                        print(f"Rate limited after {max_retries} retries. Giving up.", file=sys.stderr)
                        return {}

                # Check for other GraphQL errors
                if "errors" in result:
                    print(f"GraphQL errors: {result['errors']}", file=sys.stderr)
                    return {}

                return result.get("data", {})

            except httpx.RequestError as e:
                last_error = e
                if attempt < max_retries:
                    # Network errors also get exponential backoff
                    wait_time = initial_wait * (2 ** attempt) + random.uniform(0, 1)
                    print(f"Request error: {e}. Retrying in {wait_time:.2f} seconds (attempt {attempt + 1}/{max_retries})...", file=sys.stderr)
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"Request error after {max_retries} retries: {e}", file=sys.stderr)
                    return {}

            except json.JSONDecodeError as e:
                last_error = e
                print(f"JSON decode error: {e}", file=sys.stderr)
                return {}

        return {}

    def close(self):
        """Close the HTTP client"""
        self.client.close()

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


def get_tournaments_info() -> Dict[int, str]:
    """Get mapping of tournament IDs to names"""
    return {
        Tournament.CLASSIC: "classic",
        Tournament.SIGNALS: "signals",
        Tournament.CRYPTO: "crypto"
    }


def get_user_models(client: NumeraiGraphQLClient, tournament: Optional[int] = None) -> List[Dict]:
    """
    Get all models for the authenticated user

    Args:
        client: Authenticated GraphQL client
        tournament: Optional tournament filter

    Returns:
        List of model dictionaries with id, name, and tournament
    """
    query = """
    query GetUserModels {
        account {
            models {
                id
                name
                tournament
            }
        }
    }
    """

    result = client.query(query)

    if not result or "account" not in result or not result["account"]:
        return []

    models = result["account"].get("models", [])

    # Filter by tournament if specified
    if tournament is not None:
        models = [m for m in models if m.get("tournament") == tournament]

    return models


def get_account_models(client: NumeraiGraphQLClient, username: str, tournament: Optional[int] = None) -> List[Dict]:
    """
    Get public models for a specific user

    Args:
        client: GraphQL client (can be anonymous)
        username: Username to query
        tournament: Optional tournament filter

    Returns:
        List of model dictionaries with id, name, and tournament
    """
    query = """
    query GetAccountProfile($username: String!, $tournament: Int) {
        accountProfile(username: $username, tournament: $tournament) {
            models {
                id
                tournament
            }
        }
    }
    """

    variables = {"username": username}
    if tournament is not None:
        variables["tournament"] = tournament

    result = client.query(query, variables)
    account_data = result.get("accountProfile", {})
    models = account_data.get("models", [])

    # Add synthetic names since public models don't expose names
    for i, model in enumerate(models):
        model["name"] = f"{username}_model_{i+1}"

    return models


def get_all_users(client: NumeraiGraphQLClient, tournament: int = 8, limit: int = 1000) -> List[str]:
    """
    Get list of all usernames from leaderboard

    Args:
        client: GraphQL client
        tournament: Tournament ID
        limit: Maximum number of users to fetch

    Returns:
        List of usernames
    """
    query = """
    query GetAllUsers($tournament: Int!, $limit: Int!) {
        accountLeaderboard(
            tournament: $tournament,
            limit: $limit,
            orderBy: "mmc",
            direction: "desc"
        ) {
            username
        }
    }
    """

    variables = {"tournament": tournament, "limit": limit}
    result = client.query(query, variables)
    leaderboard = result.get("accountLeaderboard", [])

    return [account["username"] for account in leaderboard if account.get("username")]


def read_existing_users(output_file: str, output_format: str) -> Set[str]:
    """
    Read existing usernames from output file to avoid duplicates

    Args:
        output_file: Path to the output file
        output_format: Format of the output file ('csv' or 'json')

    Returns:
        Set of usernames already processed
    """
    existing_users = set()

    if not os.path.exists(output_file):
        return existing_users

    try:
        if output_format.lower() == 'csv':
            with open(output_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'username' in row:
                        existing_users.add(row['username'])

        elif output_format.lower() == 'json':
            with open(output_file, 'r') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, dict):
                        # Format: {"username:model_name": "model_id"}
                        for key in data.keys():
                            if ':' in key:
                                username = key.split(':', 1)[0]
                                existing_users.add(username)
                except json.JSONDecodeError:
                    # File exists but is empty or invalid JSON
                    pass

    except Exception as e:
        print(f"Warning: Could not read existing file {output_file}: {e}", file=sys.stderr)

    return existing_users


def append_models_to_file(models: List[Dict], output_file: str, output_format: str, is_first_write: bool = False):
    """
    Append models to output file incrementally

    Args:
        models: List of model dictionaries to append
        output_file: Path to output file
        output_format: Format ('csv' or 'json')
        is_first_write: Whether this is the first write to the file
    """
    if not models:
        return

    try:
        if output_format.lower() == 'csv':
            mode = 'w' if is_first_write else 'a'
            with open(output_file, mode, newline='') as f:
                writer = csv.writer(f)

                # Write header only on first write
                if is_first_write:
                    writer.writerow(["username", "model_name", "model_id", "tournament"])

                # Write model data
                for model in models:
                    writer.writerow([
                        model.get("username", ""),
                        model["name"],
                        model["id"],
                        model.get("tournament", "")
                    ])

        elif output_format.lower() == 'json':
            # For JSON, we need to merge with existing data
            existing_data = {}

            if not is_first_write and os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = {}

            # Add new models to existing data
            for model in models:
                key = f"{model.get('username', 'unknown')}:{model['name']}"
                existing_data[key] = model["id"]

            # Write back the complete JSON
            with open(output_file, 'w') as f:
                json.dump(existing_data, f, indent=2)

    except Exception as e:
        print(f"Error writing to file {output_file}: {e}", file=sys.stderr)


def get_all_models_for_all_users(client: NumeraiGraphQLClient, tournament: Optional[int] = None, user_limit: int = 1000,
                                request_delay: float = 0.5, output_file: Optional[str] = None,
                                output_format: str = 'csv', save_frequency: int = 1) -> List[Dict]:
    """
    Get all models for all users with incremental saving (this can be a large operation)

    Args:
        client: GraphQL client
        tournament: Optional tournament filter
        user_limit: Maximum number of users to process
        request_delay: Delay between requests in seconds to avoid rate limiting
        output_file: Optional output file for incremental saving
        output_format: Format for incremental saving ('csv', 'json', or 'table')
        save_frequency: Save after every N users processed (default: 1)

    Returns:
        List of model dictionaries with username, id, name, and tournament
    """
    print(f"Fetching up to {user_limit} users...", file=sys.stderr)
    usernames = get_all_users(client, tournament or Tournament.CLASSIC, user_limit)

    # Skip incremental saving for table format
    use_incremental_saving = output_file and output_format.lower() in ['csv', 'json']
    existing_users = set()

    if use_incremental_saving:
        existing_users = read_existing_users(output_file, output_format)
        if existing_users:
            print(f"Found existing file with {len(existing_users)} users already processed. Will skip duplicates.", file=sys.stderr)

    # Filter out users that have already been processed
    users_to_process = [u for u in usernames if u not in existing_users]
    skipped_count = len(usernames) - len(users_to_process)

    if skipped_count > 0:
        print(f"Skipping {skipped_count} users already in output file.", file=sys.stderr)

    print(f"Processing {len(users_to_process)} users. Fetching models for each user with {request_delay}s delay between requests...", file=sys.stderr)
    if use_incremental_saving:
        print(f"Saving to {output_file} every {save_frequency} user(s).", file=sys.stderr)

    all_models = []
    failed_users = []
    pending_models = []  # Buffer for incremental saving
    is_first_write = len(existing_users) == 0

    for i, username in enumerate(users_to_process, 1):
        if i % 50 == 0:
            print(f"Progress: {i}/{len(users_to_process)} users processed. Found {len(all_models)} models so far. Failed: {len(failed_users)}", file=sys.stderr)

        try:
            # Add delay between requests to be respectful to the API
            if i > 1:  # Don't delay on first request
                time.sleep(request_delay)

            user_models = get_account_models(client, username, tournament)
            if user_models:
                for model in user_models:
                    model["username"] = username
                all_models.extend(user_models)

                if use_incremental_saving:
                    pending_models.extend(user_models)

                # Save incrementally based on save_frequency
                if use_incremental_saving and len(pending_models) > 0 and i % save_frequency == 0:
                    append_models_to_file(pending_models, output_file, output_format, is_first_write)
                    is_first_write = False
                    pending_models = []  # Clear buffer after saving

        except Exception as e:
            print(f"Warning: Failed to fetch models for {username}: {e}", file=sys.stderr)
            failed_users.append(username)
            continue

    # Save any remaining models in the buffer
    if use_incremental_saving and pending_models:
        append_models_to_file(pending_models, output_file, output_format, is_first_write)

    print(f"Completed! Found {len(all_models)} total models from {len(users_to_process)} users.", file=sys.stderr)
    if failed_users:
        print(f"Failed to fetch models for {len(failed_users)} users due to errors.", file=sys.stderr)
    if skipped_count > 0:
        print(f"Skipped {skipped_count} users that were already processed.", file=sys.stderr)

    return all_models