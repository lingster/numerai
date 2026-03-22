#!/usr/bin/env bash
# Numerai GraphQL API - Common Query Examples
# Run any example directly: bash leaderboard_query.sh

API="https://api-tournament.numer.ai/"

echo "=== Current Round Info ==="
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ rounds(tournament: 8, limit: 1) { number openTime closeTime resolvedGeneral resolvedStaking payoutFactor } }"}' \
  "$API" | python3 -m json.tool

echo ""
echo "=== Top 10 Leaderboard (Classic, by Corr) ==="
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountLeaderboard(tournament: 8, limit: 10, orderBy: \"corr\", direction: \"desc\") { username rank corr mmc nmrStaked return1y } }"}' \
  "$API" | python3 -m json.tool

echo ""
echo "=== NMR/USD Price ==="
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ latestCurrencyPrice(targetSymbol: \"USD\", baseSymbol: \"NMR\") { price lastUpdated } }"}' \
  "$API" | python3 -m json.tool

echo ""
echo "=== Available Tournaments ==="
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ tournaments { id name tournament active } }"}' \
  "$API" | python3 -m json.tool

# To query a specific user's models, uncomment and set username:
# USERNAME="someuser"
# echo ""
# echo "=== Models for $USERNAME ==="
# curl -s -X POST -H "Content-Type: application/json" \
#   -d "{\"query\": \"{ accountProfile(username: \\\"$USERNAME\\\", tournament: 8) { models { id displayName tournament startDate corrRep mmcRep } } }\"}" \
#   "$API" | python3 -m json.tool

# To query a model's performance by UUID, uncomment and set model_id:
# MODEL_ID="your-model-uuid-here"
# echo ""
# echo "=== Performance for model $MODEL_ID (last 10 rounds) ==="
# curl -s -X POST -H "Content-Type: application/json" \
#   -d "{\"query\": \"{ v2RoundModelPerformances(modelId: \\\"$MODEL_ID\\\", lastNRounds: 10, tournament: 8) { roundNumber corr mmc corrPercentile mmcPercentile payout roundResolved } }\"}" \
#   "$API" | python3 -m json.tool
