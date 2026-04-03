# Crypto Tournament (ID: 12) Reference

The Crypto Signals tournament has key differences from Classic (8) and Signals (11).

## Key Differences

| Feature | Classic (8) | Crypto (12) |
|---------|-------------|-------------|
| Model lookup | `v3UserProfile(modelName)` | `accountProfile(username, tournament: 12)` |
| Performance data | Direct fields on `v2RoundModelPerformances` | `submissionScores` array |
| Model identifier | Name (string) | UUID |
| Score fields | `corr`, `mmc`, etc. (top-level) | Nested in `submissionScores` |

## Step 1: Get Crypto Models for a User

Always include `tournament: 12` — without it you get Classic models only:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountProfile(username: \"USERNAME\", tournament: 12) { username models { id displayName tournament } } }"}' \
  https://api-tournament.numer.ai/
```

Example response:
```json
{
  "data": {
    "accountProfile": {
      "username": "fish_n_chips",
      "models": [
        {"id": "b27db79e-bafa-4a76-8a75-9f91168cd222", "displayName": "fncc_t1", "tournament": 12},
        {"id": "c8a5bd73-ca3a-4b52-8d9c-68effe58e66a", "displayName": "fncc_t2", "tournament": 12}
      ]
    }
  }
}
```

## Step 2: Get Crypto Performance Data

Use `v2RoundModelPerformances` with `tournament: 12` and the model UUID:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ v2RoundModelPerformances(modelId: \"MODEL_UUID\", tournament: 12, lastNRounds: 10) { roundNumber roundResolved submissionScores { displayName value } } }"}' \
  https://api-tournament.numer.ai/
```

Example response:
```json
{
  "data": {
    "v2RoundModelPerformances": [
      {
        "roundNumber": 1163,
        "roundResolved": true,
        "submissionScores": [
          {"displayName": "corr", "value": -0.166},
          {"displayName": "mmc", "value": -0.113},
          {"displayName": "canon_corr", "value": -0.166},
          {"displayName": "canon_mmc", "value": -0.113},
          {"displayName": "season_score", "value": -0.113}
        ]
      }
    ]
  }
}
```

## Available Crypto Score Types

| displayName | Description |
|-------------|-------------|
| `corr` | Correlation score |
| `mmc` | Meta Model Contribution |
| `canon_corr` | Canonical correlation |
| `canon_mmc` | Canonical MMC |
| `apcwcm` | Average pairwise correlation weighted by crypto market cap |
| `mcwcm` | Market cap weighted correlation metric |
| `season_score` | Current season score |

## Crypto Leaderboard

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountLeaderboard(tournament: 12, limit: 10, orderBy: \"corr\", direction: \"desc\") { username rank corr mmc nmrStaked } }"}' \
  https://api-tournament.numer.ai/
```

## Complete Python Workflow

```python
import httpx

API_URL = "https://api-tournament.numer.ai/"

def gql(query, variables=None):
    resp = httpx.post(API_URL, json={"query": query, "variables": variables or {}})
    resp.raise_for_status()
    return resp.json()

username = "fish_n_chips"

# Step 1: Get crypto models
result = gql(f'{{ accountProfile(username: "{username}", tournament: 12) {{ models {{ id displayName }} }} }}')
models = result["data"]["accountProfile"]["models"]
print(f"Found {len(models)} crypto models")

# Step 2: Get performance for first model
model_id = models[0]["id"]
model_name = models[0]["displayName"]

perf = gql(f'''{{
  v2RoundModelPerformances(modelId: "{model_id}", tournament: 12, lastNRounds: 10) {{
    roundNumber
    roundResolved
    submissionScores {{ displayName value }}
  }}
}}''')

# Step 3: Extract scores
for round_data in perf["data"]["v2RoundModelPerformances"]:
    scores = {s["displayName"]: s["value"] for s in round_data["submissionScores"]}
    corr = scores.get("corr")
    mmc = scores.get("mmc")
    print(f"Round {round_data['roundNumber']}: corr={corr:.4f}, mmc={mmc:.4f}")
```

## Common Pitfalls

1. **Omitting `tournament: 12`** — `accountProfile` returns Classic models by default
2. **Using top-level score fields** — Crypto uses `submissionScores` array, not `corr`/`mmc` directly
3. **Using model name instead of UUID** — Crypto requires UUID for `v2RoundModelPerformances`
