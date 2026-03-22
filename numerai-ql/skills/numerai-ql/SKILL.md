---
name: numerai-ql
description: This skill should be used when the user asks to "query numerai", "get model performance", "check leaderboard", "get round data", "fetch numerai scores", "query graphql api", "get numerai tournament data", "check model scores", "get payout data", "look up numerai model", "get corr score", "get mmc score", "check numerai rank", or wants to retrieve any data from the Numerai Tournament API.
version: 1.0.0
---

# Numerai GraphQL Query Skill

This skill enables querying the Numerai Tournament GraphQL API at `https://api-tournament.numer.ai/` to retrieve tournament data, model performance, leaderboards, round information, and more.

## API Overview

- **Endpoint**: `https://api-tournament.numer.ai/`
- **Method**: POST with JSON body `{"query": "...", "variables": {...}}`
- **Auth**: Most queries are public; private account data requires auth tokens
- **Tournaments**: 8 = Classic Numerai, 11 = Signals, 12 = Crypto

## Core Workflow

### Step 1: Identify What the User Wants

Map user requests to the right query:

| User Wants | Query to Use |
|------------|--------------|
| Model scores/performance | `v2RoundModelPerformances` |
| User profile or models | `accountProfile` |
| Leaderboard rankings | `accountLeaderboard` |
| Round info (open/closed) | `rounds` |
| Current NMR price | `latestCurrencyPrice` |
| Dataset links | `listDatasets` |
| Full round breakdown | `roundDetails` |
| Daily intra-round scores | `v2RoundModelPerformances` + `intraRoundSubmissionScores` |

### Step 2: Resolve Model ID (when needed)

Many performance queries require a model UUID, not a name. To get it:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountProfile(username: \"USERNAME\", tournament: 8) { models { id displayName tournament } } }"}' \
  https://api-tournament.numer.ai/
```

**Critical**: Use `displayName` (not `name`) on `ModelProfile` objects returned by `accountProfile`.

### Step 3: Execute the Query

Use the Bash tool to run curl commands against the API. Always use:
- `-X POST`
- `-H "Content-Type: application/json"`
- `-d '{"query": "...", "variables": {...}}'`

### Step 4: Parse and Present Results

Extract the relevant fields from `data.<queryName>` in the JSON response.

## Common Query Templates

### Get Current Round
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ rounds(tournament: 8, limit: 1) { number openTime closeTime resolvedGeneral resolvedStaking } }"}' \
  https://api-tournament.numer.ai/
```

### Get User Models
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountProfile(username: \"USERNAME\", tournament: 8) { models { id displayName tournament } } }"}' \
  https://api-tournament.numer.ai/
```

### Get Model Performance (last N rounds)
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ v2RoundModelPerformances(modelId: \"MODEL_UUID\", tournament: 8, lastNRounds: 20) { roundNumber corr mmc fnc tc corrPercentile mmcPercentile roundResolved payout } }"}' \
  https://api-tournament.numer.ai/
```

### Get Leaderboard Top 10
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountLeaderboard(tournament: 8, limit: 10, orderBy: \"corr\", direction: \"desc\") { username rank corr mmc nmrStaked return1y } }"}' \
  https://api-tournament.numer.ai/
```

### Get NMR Price
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "query { latestCurrencyPrice(targetSymbol: \"USD\", baseSymbol: \"NMR\") { price lastUpdated } }"}' \
  https://api-tournament.numer.ai/
```

### Get Daily Scores (Intra-Round)
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "query": "query { v2RoundModelPerformances(modelId: \"MODEL_UUID\", roundNumber__eq: ROUND_NUM, tournament: 8) { roundNumber roundResolved atRisk intraRoundSubmissionScores { displayName value percentile day date payoutPending } } }"
  }' \
  https://api-tournament.numer.ai/
```

## Key Type Distinctions

### Model vs ModelProfile

| Context | Type | Use field |
|---------|------|-----------|
| `account.models` | `Model` | `name` |
| `model(modelId)` | `Model` | `name` |
| `accountProfile.models` | `ModelProfile` | `displayName` |

### Crypto Tournament Differences (Tournament 12)

- Always pass `tournament: 12` to `accountProfile` to get crypto models
- Performance scores are in `submissionScores` array (not top-level fields):
  ```
  submissionScores { displayName value }
  # displayName: "corr", "mmc", "canon_corr", "canon_mmc", "season_score"
  ```

## Error Handling

GraphQL errors appear in the `errors` array alongside `data`. Always check:
```python
response = response.json()
if "errors" in response:
    # handle error
data = response.get("data", {})
```

## Python Helper Pattern

For multi-step workflows, use `httpx` or `requests`:

```python
import httpx

API_URL = "https://api-tournament.numer.ai/"

def gql(query, variables=None):
    resp = httpx.post(API_URL, json={"query": query, "variables": variables or {}})
    return resp.json()

# Get model ID
result = gql('{ accountProfile(username: "myuser", tournament: 8) { models { id displayName } } }')
model_id = result["data"]["accountProfile"]["models"][0]["id"]

# Get performance
perf = gql(
    "{ v2RoundModelPerformances(modelId: $id, lastNRounds: 10) { roundNumber corr mmc payout } }",
    {"id": model_id}
)
```

## Additional Resources

- **`references/api-reference.md`** — Full query reference with all parameters and field definitions
- **`references/crypto-tournament.md`** — Crypto tournament (ID 12) specific patterns
- **`references/intra-round.md`** — Daily intra-round score queries and data structure
- **`examples/get_model_performance.py`** — Complete Python script for fetching model performance
- **`examples/leaderboard_query.sh`** — Shell script examples for common queries
- **`scripts/query.sh`** — Reusable curl wrapper for the Numerai API
