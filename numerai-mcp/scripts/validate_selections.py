#!/usr/bin/env python3
"""
Validate that every GraphQL selection set in tools_queries.py and
tools_mutations.py references fields that exist in the live schema.

Strategy:
  1. Extract every triple-quoted string from the tool files.
  2. Strip variable declarations and arg blocks.
  3. Find the outermost `{ ... }` and walk it as a selection-set tree.
  4. For each field, check it exists on the parent GraphQL type.

Usage:
    python scripts/validate_selections.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
INTROSPECTION = REPO_ROOT / ".schema" / "introspection.json"
TOOLS_DIR = REPO_ROOT / "numerai-mcp" / "numerai_mcp_pkg"


def load_schema() -> dict:
    data = json.loads(INTROSPECTION.read_text())["data"]["__schema"]
    return {t["name"]: t for t in data["types"]}


def inner_named(t: dict) -> str:
    while t.get("ofType") is not None:
        t = t["ofType"]
    return t["name"] or ""


def field_lookup(by_name: dict, type_name: str) -> dict[str, dict]:
    t = by_name.get(type_name)
    if not t:
        return {}
    fields = t.get("fields") or t.get("inputFields") or []
    return {f["name"]: f for f in fields}


# Tokenize: '{', '}', identifier, ':', '(', ')'.
TOKEN_RE = re.compile(r"\{|\}|\(|\)|[A-Za-z_][\w]*|:")


def tokenize(s: str) -> list[str]:
    # Drop $-vars, commas, fragments, etc. that we don't care about.
    s = re.sub(r"\$[A-Za-z_]\w*", "", s)
    s = s.replace(",", " ")
    return TOKEN_RE.findall(s)


def parse_selection_set(tokens: list[str], idx: int) -> tuple[list[dict], int]:
    """Parse '{ ... }' starting at tokens[idx] == '{'. Returns (children, idx_after_brace)."""
    assert tokens[idx] == "{", f"expected '{{', got {tokens[idx]}"
    idx += 1
    children: list[dict] = []
    while idx < len(tokens):
        tok = tokens[idx]
        if tok == "}":
            return children, idx + 1
        if tok == "{":
            # Inline selection set without a field — skip (shouldn't happen).
            _, idx = parse_selection_set(tokens, idx)
            continue
        # Identifier — could be `name` or `alias: name`.
        if not re.match(r"[A-Za-z_]", tok):
            idx += 1
            continue
        # Look ahead for alias.
        if idx + 1 < len(tokens) and tokens[idx + 1] == ":":
            real_name = tokens[idx + 2]
            idx += 3
        else:
            real_name = tok
            idx += 1
        # Skip optional args (...).
        if idx < len(tokens) and tokens[idx] == "(":
            depth = 1
            idx += 1
            while idx < len(tokens) and depth > 0:
                if tokens[idx] == "(":
                    depth += 1
                elif tokens[idx] == ")":
                    depth -= 1
                idx += 1
        # Optional nested selection set.
        if idx < len(tokens) and tokens[idx] == "{":
            sub, idx = parse_selection_set(tokens, idx)
            children.append({"name": real_name, "children": sub})
        else:
            children.append({"name": real_name, "children": []})
    return children, idx


def parse_query(body: str) -> tuple[bool, list[dict]]:
    """Return (is_mutation, top_level_fields)."""
    is_mutation = bool(re.match(r"^\s*mutation\b", body))
    tokens = tokenize(body)
    # Find first '{' — that's the start of the top-level selection set.
    try:
        start = tokens.index("{")
    except ValueError:
        return is_mutation, []
    fields, _ = parse_selection_set(tokens, start)
    return is_mutation, fields


def walk(by_name: dict, type_name: str, nodes: list[dict], path: str, errors: list[str]) -> None:
    fields = field_lookup(by_name, type_name)
    if not fields:
        if nodes:
            errors.append(f"{path}: cannot resolve fields on unknown type `{type_name}`")
        return
    for n in nodes:
        fname = n["name"]
        if fname not in fields:
            errors.append(f"{path}: field `{fname}` not on type `{type_name}`")
            continue
        child_type = inner_named(fields[fname]["type"])
        child_kind = by_name.get(child_type, {}).get("kind")
        # OBJECT and INTERFACE need a selection set; SCALAR/ENUM/UNION-of-scalars don't.
        if child_kind in ("OBJECT", "INTERFACE") and not n["children"]:
            errors.append(
                f"{path}.{fname}: field returns OBJECT `{child_type}` but no sub-selection provided"
            )
            continue
        if child_kind in ("SCALAR", "ENUM") and n["children"]:
            errors.append(
                f"{path}.{fname}: field returns scalar `{child_type}` — should not have sub-selection"
            )
            continue
        if n["children"]:
            walk(by_name, child_type, n["children"], f"{path}.{fname}", errors)


GRAPHQL_RE = re.compile(r'"""(.*?)"""', re.DOTALL)


def validate_file(path: pathlib.Path, by_name: dict) -> list[str]:
    errors: list[str] = []
    text = path.read_text()
    for m in GRAPHQL_RE.finditer(text):
        body = m.group(1).strip()
        if not body or "{" not in body:
            continue
        # Skip non-query docstrings (heuristic: must contain a top-level query
        # or mutation keyword OR start with '{').
        if not re.match(r"^\s*(query|mutation|\{)", body):
            continue
        is_mut, fields = parse_query(body)
        root = "RootMutationType" if is_mut else "RootQueryType"
        snippet = re.sub(r"\s+", " ", body)[:50]
        walk(by_name, root, fields, f"{path.name}({snippet})", errors)
    return errors


def main() -> int:
    by_name = load_schema()
    all_errors: list[str] = []
    for fn in ["tools_queries.py", "tools_mutations.py"]:
        path = TOOLS_DIR / fn
        all_errors.extend(validate_file(path, by_name))

    if all_errors:
        for e in all_errors:
            print(e)
        print(f"\n{len(all_errors)} errors")
        return 1
    print("OK — all selections valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
