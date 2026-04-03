#!/usr/bin/env bash
# Numerai GraphQL API query wrapper
#
# Usage:
#   ./query.sh '<graphql query>'
#   ./query.sh '<graphql query>' '{"var": "value"}'
#
# Examples:
#   ./query.sh '{ rounds(tournament: 8, limit: 1) { number openTime closeTime } }'
#   ./query.sh '{ accountProfile(username: "myuser", tournament: 8) { models { id displayName } } }'
#   ./query.sh 'query($id: String!) { v2RoundModelPerformances(modelId: $id, lastNRounds: 5) { roundNumber corr mmc } }' '{"id": "your-model-uuid"}'

set -euo pipefail

API_URL="https://api-tournament.numer.ai/"
QUERY="${1:-}"
VARIABLES="${2:-}"

if [[ -z "$QUERY" ]]; then
  echo "Usage: $0 '<graphql query>' ['<variables json>']" >&2
  exit 1
fi

if [[ -n "$VARIABLES" ]]; then
  PAYLOAD=$(printf '{"query": %s, "variables": %s}' "$(echo "$QUERY" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')" "$VARIABLES")
else
  PAYLOAD=$(printf '{"query": %s}' "$(echo "$QUERY" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')")
fi

curl -s -X POST \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" \
  "$API_URL" | python3 -m json.tool
