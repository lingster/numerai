---
name: numerai-graphql-query
description: >
  Use this skill when the user asks to run, execute, or construct a GraphQL query
  against the Numerai API. Triggers: "query numerai", "run a graphql query",
  "get model scores", "fetch leaderboard", "check round", "get corr/mmc/tc scores",
  "look up model performance", "what is the NMR price", "list datasets", or any
  request to retrieve data from https://api-tournament.numer.ai/.
version: 1.0.0
---

# Numerai GraphQL Query Skill

Endpoint: `https://api-tournament.numer.ai/`  
Schema: `/home/user/numerai/graphql-schema-extractor/schema.graphql`  
Query tool: `/home/user/numerai/graphql-schema-extractor/query` (Go binary)

## How to Run a Query

### Using the Go tool (preferred)
```bash
cd /home/user/numerai/graphql-schema-extractor

# Public query
./query '<gql>'

# With variables
./query 'query($id: ID!) { v2RoundModelPerformances(modelId: $id, lastNRounds: 5) { roundNumber corr mmc } }' '{"id": "model-uuid"}'

# Authenticated (account-private data)
NUMERAI_TOKEN=<token> ./query '{ account { username availableNmr } }'
# or
./query -auth <token> '{ account { username availableNmr } }'

# Raw JSON output (no pretty print)
./query -raw '<gql>'
```

If the binary is missing, rebuild it:
```bash
cd /home/user/numerai/graphql-schema-extractor && go build ./cmd/query/
```

### Using curl (alternative)
```bash
curl -s -X POST https://api-tournament.numer.ai/ \
  -H "Content-Type: application/json" \
  -d '{"query": "{ rounds(tournament: 8, limit: 1) { number openTime } }"}' \
  | python3 -m json.tool
```

## Tournament IDs

| ID | Tournament |
|----|------------|
| 8  | Classic (Numerai) |
| 11 | Signals |
| 12 | Crypto |

## Step-by-step: Queries That Need a Model UUID

Many performance queries require a model UUID (`ID`), not a username. Resolve it first:

```bash
./query '{ accountProfile(username: "USERNAME", tournament: 8) { models { id displayName } } }'
```

Then use the `id` in follow-up queries.

## Common Query Templates

### Current round
```graphql
{ rounds(tournament: 8, limit: 1) { number openTime closeTime resolvedGeneral resolvedStaking } }
```

### Account models
```graphql
{ accountProfile(username: "USERNAME", tournament: 8) { models { id displayName tournament } } }
```

### Model performance (last N rounds)
```graphql
{
  v2RoundModelPerformances(modelId: "MODEL_UUID", tournament: 8, lastNRounds: 20) {
    roundNumber roundResolved roundOpenTime
    corr corrPercentile mmc mmcPercentile tc tcPercentile
    payout atRisk
  }
}
```

### Model performance for a specific round
```graphql
{
  v2RoundModelPerformances(modelId: "MODEL_UUID", roundNumberEq: 1252, tournament: 8) {
    roundNumber corr mmc tc
    submissionScores { displayName value percentile day }
    intraRoundSubmissionScores { displayName value percentile day date }
  }
}
```

### Public model profile
```graphql
{
  v3UserProfile(modelName: "MODEL_NAME", tournament: 8) {
    username stakeValue nmrStaked
    latestRanks { corr mmc tc }
    latestReps  { corr mmc tc }
    latestReturns { oneDay threeMonths oneYear allTime }
  }
}
```

### Leaderboard (top N)
```graphql
{
  accountLeaderboard(tournament: 8, limit: 10, orderBy: "corr", direction: "desc") {
    username rank corr mmc tc nmrStaked return1y
  }
}
```

### Signals leaderboard
```graphql
{
  signalsLeaderboard(limit: 10, orderBy: "corrRep", direction: "desc") {
    username rank corrRep mmcRep tcRep nmrStaked return52Weeks
  }
}
```

### NMR price
```graphql
{ latestCurrencyPrice(baseSymbol: "NMR", targetSymbol: "USD") { price lastUpdated } }
```

### List datasets for a round
```graphql
{ listDatasets(tournament: 8, round: 1252) }
```

### Dataset download URL
```graphql
{ dataset(filename: "v5/live.parquet", tournament: 8) }
```

### Round details (all model scores)
```graphql
{
  roundDetails(roundNumber: 1252, tournament: 8) {
    roundNumber roundResolved totalAtStake totalPayout totalBurned
    models { modelName corr corrPercentile mmc mmcPercentile tc tcPercentile payoutPending payoutSettled }
  }
}
```

### Pipeline status
```graphql
{ pipelineStatus(tournament: "classic") { isScoringDay scoredAt resolvedAt dataReadyAt } }
```

### Pending payouts (authenticated)
```graphql
{ pendingModelPayouts(tournament: 8) { pending { modelName roundNumber payoutNmr } } }
```

### My account info (authenticated)
```graphql
{ account { username availableNmr status models(showArchived: false) { name tournament v2Stake { stakeValue status } } } }
```

## Score Metric Glossary

| Field | Meaning |
|-------|---------|
| `corr` | Correlation with target |
| `corrV4` | Correlation v4 (feature-neutral) |
| `corr60` / `corr20` | 60/20-day rolling correlation |
| `mmc` | Meta-model contribution |
| `mmc60` | 60-day rolling MMC |
| `tc` | True contribution |
| `fnc` / `fncV3` / `fncV4` | Feature neutral correlation variants |
| `ic` / `icV2` | Information coefficient |
| `alpha` | Alpha score |
| `bmc` | Beta-adjusted MMC |
| `ric` | Rank information coefficient |
| `mpc` | Meta portfolio contribution |
| `apy` | Annualised percentage yield |
| `*Rep` | Reputation — rolling weighted average of the metric |
| `*Percentile` | Percentile rank among all submissions that round |
| `*Rank` | Integer rank on leaderboard |

## Field Notes

- `Model.name` vs `ModelProfile.displayName` — `accountProfile.models` returns `ModelProfile`; use `displayName` there, `name` on `Model`.
- Crypto tournament (12): scores live inside `submissionScores { displayName value }` — `displayName` values are `"corr"`, `"mmc"`, `"canon_corr"`, `"canon_mmc"`, `"season_score"`.
- `v2RoundModelPerformances` arguments accept camelCase: `roundNumberEq`, `roundNumberGte`, `roundNumberLte`, `lastNRounds`, `resolvedOnly`, `resolvedWithinLastNDays`, `scoredWithinLastNDays`.
- Authentication: pass `Authorization: Token <secret_key>` header. The `secretKey` is returned only when creating a token via `createApiToken` mutation.

## Checking the Schema

When unsure what fields a type has, check the extracted schema:
```bash
grep -A 30 '^type ModelData' /home/user/numerai/graphql-schema-extractor/schema.graphql
grep -A 10 '^type Round ' /home/user/numerai/graphql-schema-extractor/schema.graphql
```

Or re-extract it (updates the file in place):
```bash
cd /home/user/numerai/graphql-schema-extractor && go run main.go > schema.graphql
```
