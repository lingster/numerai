#!/usr/bin/env bash
# Fetch a fresh GraphQL introspection result from api-tournament.numer.ai.
# Output: ../../.schema/introspection.json (repo root /.schema/)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/.schema"
QUERY="$SCHEMA_DIR/introspect_query.gql"
OUT="$SCHEMA_DIR/introspection.json"

mkdir -p "$SCHEMA_DIR"

if [[ ! -f "$QUERY" ]]; then
  echo "Missing introspection query at $QUERY" >&2
  exit 1
fi

curl -sS -X POST \
  -H "Content-Type: application/json" \
  --data-binary "@<(jq -n --rawfile q "$QUERY" '{query: \$q}')" \
  https://api-tournament.numer.ai/ -o "$OUT"

echo "wrote $OUT ($(wc -c <"$OUT") bytes)"
