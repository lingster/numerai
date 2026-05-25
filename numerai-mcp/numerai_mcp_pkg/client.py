"""GraphQL HTTP client + auth helpers for the Numerai tournament API."""

from __future__ import annotations

import json
import logging
import os
import sys
from typing import Any, Optional, Type, TypeVar

import httpx
from pydantic import BaseModel

NUMERAI_API_URL = "https://api-tournament.numer.ai/"

_logger = logging.getLogger("numerai-mcp")
if not _logger.handlers:
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

_http_client = httpx.Client(timeout=30.0)


def auth_header() -> Optional[str]:
    public_id = os.getenv("NUMERAI_PUBLIC_ID") or os.getenv("NUMERAI_API_PUBLIC_ID")
    secret_key = os.getenv("NUMERAI_SECRET_KEY") or os.getenv("NUMERAI_API_SECRET_KEY")
    if public_id and secret_key:
        return f"Token {public_id}${secret_key}"
    return None


def _build_headers(use_auth: bool) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if use_auth:
        token = auth_header()
        if token:
            headers["Authorization"] = token
    return headers


def post_graphql(
    query: str,
    variables: Optional[dict[str, Any]] = None,
    use_auth: bool = True,
    drop_none_vars: bool = True,
) -> dict[str, Any]:
    """Run a GraphQL query and return the parsed JSON response (or error dict).

    `drop_none_vars`: if True (default), variables with value None are stripped
    before sending. This avoids 500s from filter-style args (e.g.
    `roundNumber__eq=None`) where the server treats explicit null differently
    from "argument not provided." Pass `drop_none_vars=False` when you need to
    send `null` to clear a server-side value (rare; relevant to a few
    mutations).
    """
    payload: dict[str, Any] = {"query": query}
    if variables is not None:
        if drop_none_vars:
            variables = {k: v for k, v in variables.items() if v is not None}
        payload["variables"] = variables

    try:
        response = _http_client.post(
            NUMERAI_API_URL, headers=_build_headers(use_auth), json=payload
        )
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


T = TypeVar("T", bound=BaseModel)


def extract(response: dict[str, Any], path: str) -> Any:
    """Pull a dotted path out of a GraphQL response's `data` block.

    Returns None if any segment is missing. Errors and http_error pass through
    untouched at the top level — call sites that want the raw envelope should
    not use this helper.
    """
    if "errors" in response or "http_error" in response:
        return None
    cur: Any = response.get("data")
    for seg in path.split("."):
        if cur is None:
            return None
        if isinstance(cur, list):
            return cur
        cur = cur.get(seg)
    return cur


def parse(
    response: dict[str, Any],
    path: str,
    model: Type[T],
) -> dict[str, Any]:
    """Parse a GraphQL response at the given path into a pydantic model.

    Returns a dict envelope `{ "data": <model dict>, "raw": <full response> }`.
    On error, returns `{ "errors": ..., "raw": ... }`.

    Lists are mapped element-wise.
    """
    if "errors" in response:
        return {"errors": response["errors"], "raw": response}
    if "http_error" in response:
        return {"errors": [response], "raw": response}

    payload = extract(response, path)
    if payload is None:
        return {"data": None, "raw": response}

    if isinstance(payload, list):
        parsed = [model.model_validate(item).model_dump(by_alias=True, exclude_none=True) for item in payload]
    else:
        parsed = model.model_validate(payload).model_dump(by_alias=True, exclude_none=True)
    return {"data": parsed}
