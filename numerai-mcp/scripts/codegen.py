#!/usr/bin/env python3
"""
Codegen for numerai-mcp.

Reads a GraphQL introspection result and emits:

  - numerai_mcp_pkg/models.py     pydantic models (one per OBJECT/ENUM/INPUT_OBJECT type)
  - ../docs/numerai_graphql_schema.md   full schema reference

The introspection JSON is fetched from .schema/introspection.json by default. To
refresh, see scripts/introspect.sh (or re-run that script before this one).
"""

from __future__ import annotations

import argparse
import json
import keyword
import pathlib
from dataclasses import dataclass
from typing import Any

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
DEFAULT_INTROSPECTION = REPO_ROOT / ".schema" / "introspection.json"
DEFAULT_MODELS_OUT = REPO_ROOT / "numerai-mcp" / "numerai_mcp_pkg" / "models.py"
DEFAULT_DOC_OUT = REPO_ROOT / "docs" / "numerai_graphql_schema.md"

SCALAR_MAP = {
    "Boolean": "bool",
    "Int": "int",
    "Float": "float",
    "String": "str",
    "ID": "str",
    "Date": "str",
    "Time": "str",
    "Nmr": "str",
    "Usd": "str",
}

PY_RESERVED = set(keyword.kwlist) | {"from", "class", "global", "lambda"}


@dataclass
class TypeRef:
    """Unwraps NON_NULL / LIST wrappers into (inner_name, python_type)."""

    raw: dict

    def render(self) -> str:
        return self._render(self.raw)

    @classmethod
    def _render(cls, t: dict) -> str:
        kind = t["kind"]
        if kind == "NON_NULL":
            return cls._render(t["ofType"])
        if kind == "LIST":
            return f"list[{cls._render(t['ofType'])}]"
        name = t["name"]
        if name in SCALAR_MAP:
            return SCALAR_MAP[name]
        return f'"{name}"'

    @classmethod
    def named(cls, t: dict) -> str:
        """Return the innermost named type."""
        while t.get("ofType") is not None:
            t = t["ofType"]
        return t["name"] or ""

    @classmethod
    def render_signature(cls, t: dict) -> str:
        """GraphQL-style signature: [String!]! → '[String!]!'."""
        kind = t["kind"]
        if kind == "NON_NULL":
            return cls.render_signature(t["ofType"]) + "!"
        if kind == "LIST":
            return "[" + cls.render_signature(t["ofType"]) + "]"
        return t["name"]


def safe_field_name(name: str) -> tuple[str, bool]:
    """Return (python_name, needs_alias)."""
    if name in PY_RESERVED:
        return name + "_", True
    return name, False


def gen_enum(t: dict) -> str:
    lines = [f'class {t["name"]}(str, Enum):']
    if t.get("description"):
        lines.append(f'    """{t["description"]}"""')
    values = t.get("enumValues") or []
    if not values:
        lines.append("    pass")
    for v in values:
        member = v["name"]
        # Enum members keep their GraphQL name; they're already SCREAMING_SNAKE in this API.
        lines.append(f'    {member} = "{member}"')
    return "\n".join(lines)


def gen_object(t: dict) -> str:
    cls = t["name"]
    lines = [f"class {cls}(BaseModel):"]
    if t.get("description"):
        lines.append(f'    """{t["description"]}"""')
    lines.append("    model_config = ConfigDict(populate_by_name=True, extra='ignore')")
    fields = t.get("fields") or t.get("inputFields") or []
    if not fields:
        lines.append("    pass")
        return "\n".join(lines)
    for f in fields:
        py_name, needs_alias = safe_field_name(f["name"])
        py_type = TypeRef(f["type"]).render()
        # Everything optional — GraphQL responses depend on the selection set.
        py_type = f"Optional[{py_type}]"
        if needs_alias:
            lines.append(f'    {py_name}: {py_type} = Field(default=None, alias="{f["name"]}")')
        else:
            lines.append(f"    {py_name}: {py_type} = None")
    return "\n".join(lines)


def gen_models(schema: dict) -> str:
    types = schema["types"]
    enums = [t for t in types if t["kind"] == "ENUM" and not t["name"].startswith("__")]
    objects = [t for t in types if t["kind"] == "OBJECT" and not t["name"].startswith("__")]
    inputs = [t for t in types if t["kind"] == "INPUT_OBJECT"]

    enums.sort(key=lambda t: t["name"])
    objects.sort(key=lambda t: t["name"])
    inputs.sort(key=lambda t: t["name"])

    header = '''"""
Pydantic models generated from the Numerai GraphQL schema.

DO NOT EDIT BY HAND. Regenerate with:

    python scripts/codegen.py

All fields are Optional because a GraphQL response only contains the fields
named in the selection set. Custom scalars (Nmr, Usd, Date, Time) are mapped
to str — they come back as strings from the API.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
'''
    parts = [header]

    parts.append("# --- Enums ---\n")
    for t in enums:
        parts.append(gen_enum(t))
        parts.append("")

    parts.append("# --- Input objects ---\n")
    for t in inputs:
        parts.append(gen_object(t))
        parts.append("")

    parts.append("# --- Object types ---\n")
    for t in objects:
        parts.append(gen_object(t))
        parts.append("")

    # Resolve forward refs at the bottom.
    parts.append("# --- Resolve forward references ---")
    parts.append("_module_globals = dict(globals())")
    for t in objects + inputs:
        parts.append(f"{t['name']}.model_rebuild(_types_namespace=_module_globals)")
    parts.append("")

    return "\n".join(parts)


def md_type_ref(t: dict) -> str:
    name = TypeRef.named(t)
    sig = TypeRef.render_signature(t)
    if name in SCALAR_MAP or name in ("Boolean", "Int", "Float", "String", "ID"):
        return f"`{sig}`"
    return f"[`{sig}`](#{name.lower()})"


def gen_doc(schema: dict) -> str:
    types = schema["types"]
    query_type = schema["queryType"]["name"]
    mutation_type = schema["mutationType"]["name"] if schema.get("mutationType") else None

    by_name = {t["name"]: t for t in types}
    queries = (by_name[query_type].get("fields") or [])
    mutations = (by_name[mutation_type].get("fields") or []) if mutation_type else []

    enums = sorted(
        (t for t in types if t["kind"] == "ENUM" and not t["name"].startswith("__")),
        key=lambda t: t["name"],
    )
    objects = sorted(
        (t for t in types if t["kind"] == "OBJECT" and not t["name"].startswith("__")
         and t["name"] not in (query_type, mutation_type)),
        key=lambda t: t["name"],
    )
    inputs = sorted(
        (t for t in types if t["kind"] == "INPUT_OBJECT"),
        key=lambda t: t["name"],
    )
    scalars = sorted(
        (t for t in types if t["kind"] == "SCALAR" and not t["name"].startswith("__")),
        key=lambda t: t["name"],
    )

    out: list[str] = []
    out.append("# Numerai GraphQL Schema Reference\n")
    out.append("> **Generated** from `.schema/introspection.json` by `numerai-mcp/scripts/codegen.py`.\n"
               "> Do not edit by hand. Re-run the codegen after the upstream schema changes.\n")
    out.append("Endpoint: `https://api-tournament.numer.ai/`\n")
    out.append(f"- Queries: **{len(queries)}**")
    out.append(f"- Mutations: **{len(mutations)}**")
    out.append(f"- Object types: **{len(objects)}**")
    out.append(f"- Input objects: **{len(inputs)}**")
    out.append(f"- Enums: **{len(enums)}**")
    out.append(f"- Custom scalars: **{len(scalars)}**\n")

    # Index
    out.append("## Contents\n")
    out.append("- [Queries](#queries)")
    out.append("- [Mutations](#mutations)")
    out.append("- [Object types](#object-types)")
    out.append("- [Input objects](#input-objects)")
    out.append("- [Enums](#enums)")
    out.append("- [Scalars](#scalars)\n")

    def render_field(f: dict) -> list[str]:
        lines = [f"### `{f['name']}`"]
        if f.get("description"):
            lines.append(f["description"])
        lines.append("")
        lines.append(f"**Returns:** {md_type_ref(f['type'])}")
        args = f.get("args") or []
        if args:
            lines.append("")
            lines.append("**Args:**")
            lines.append("")
            lines.append("| Name | Type | Default | Description |")
            lines.append("|------|------|---------|-------------|")
            for a in args:
                desc = (a.get("description") or "").replace("\n", " ").replace("|", "\\|")
                default = a.get("defaultValue")
                default_md = f"`{default}`" if default is not None else ""
                lines.append(f"| `{a['name']}` | {md_type_ref(a['type'])} | {default_md} | {desc} |")
        lines.append("")
        return lines

    out.append("## Queries\n")
    for f in sorted(queries, key=lambda x: x["name"]):
        out.extend(render_field(f))

    if mutations:
        out.append("## Mutations\n")
        for f in sorted(mutations, key=lambda x: x["name"]):
            out.extend(render_field(f))

    def render_object(t: dict) -> list[str]:
        lines = [f"### `{t['name']}`", "", f"<a id=\"{t['name'].lower()}\"></a>"]
        if t.get("description"):
            lines.append(t["description"])
        lines.append("")
        fields = t.get("fields") or t.get("inputFields") or []
        if not fields:
            lines.append("_No fields._")
            lines.append("")
            return lines
        lines.append("| Field | Type | Description |")
        lines.append("|-------|------|-------------|")
        for f in fields:
            desc = (f.get("description") or "").replace("\n", " ").replace("|", "\\|")
            lines.append(f"| `{f['name']}` | {md_type_ref(f['type'])} | {desc} |")
        lines.append("")
        return lines

    out.append("## Object types\n")
    for t in objects:
        out.extend(render_object(t))

    out.append("## Input objects\n")
    for t in inputs:
        out.extend(render_object(t))

    out.append("## Enums\n")
    for t in enums:
        out.append(f"### `{t['name']}`")
        out.append("")
        out.append(f"<a id=\"{t['name'].lower()}\"></a>")
        if t.get("description"):
            out.append(t["description"])
            out.append("")
        out.append("| Value | Description |")
        out.append("|-------|-------------|")
        for v in t.get("enumValues") or []:
            desc = (v.get("description") or "").replace("\n", " ").replace("|", "\\|")
            out.append(f"| `{v['name']}` | {desc} |")
        out.append("")

    out.append("## Scalars\n")
    for t in scalars:
        desc = (t.get("description") or "").replace("\n", " ")
        out.append(f"- `{t['name']}` — {desc or '(no description)'}")
    out.append("")

    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--introspection", type=pathlib.Path, default=DEFAULT_INTROSPECTION)
    ap.add_argument("--models-out", type=pathlib.Path, default=DEFAULT_MODELS_OUT)
    ap.add_argument("--doc-out", type=pathlib.Path, default=DEFAULT_DOC_OUT)
    args = ap.parse_args()

    data: dict[str, Any] = json.loads(args.introspection.read_text())
    schema = data["data"]["__schema"]

    args.models_out.parent.mkdir(parents=True, exist_ok=True)
    args.doc_out.parent.mkdir(parents=True, exist_ok=True)

    args.models_out.write_text(gen_models(schema))
    args.doc_out.write_text(gen_doc(schema))
    print(f"wrote {args.models_out}")
    print(f"wrote {args.doc_out}")


if __name__ == "__main__":
    main()
