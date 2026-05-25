# Numerai GraphQL API Documentation

The Numerai Tournament API provides a comprehensive GraphQL endpoint for accessing tournament data, model information, performance metrics, and more.

> **Full schema reference (auto-generated):** [`docs/numerai_graphql_schema.md`](docs/numerai_graphql_schema.md) — every query, mutation, object type, enum and scalar with arg signatures and field tables. Regenerate with `python numerai-mcp/scripts/codegen.py` after the upstream schema changes.
>
> This hand-written document is the curated user guide — it covers the workflows callers actually use. The auto-generated reference is the authoritative type/field listing.

## Endpoint
- **URL**: `https://api-tournament.numer.ai/`
- **Method**: POST
- **Content-Type**: `application/json`

## Authentication
Most queries work without authentication, but some require API tokens for accessing private user data.

## Basic Query Structure

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "YOUR_GRAPHQL_QUERY_HERE"}' \
  https://api-tournament.numer.ai/
```

## Schema Introspection

The API supports full GraphQL introspection. Use these queries to explore the schema:

```bash
# Get all available queries
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ __schema { queryType { fields { name description args { name type { name } defaultValue } } } } }"}' \
  https://api-tournament.numer.ai/

# Get all available types
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ __schema { types { name kind } } }"}' \
  https://api-tournament.numer.ai/

# Get specific type details (replace "TypeName")
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ __type(name: \"TypeName\") { fields { name type { name kind } } } }"}' \
  https://api-tournament.numer.ai/
```

## Available Tournaments

Get a list of all available tournaments:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ tournaments { id name tournament active } }"}' \
  https://api-tournament.numer.ai/
```

**Response:**
```json
{
  "data": {
    "tournaments": [
      {"id": "1a868e3e-1df7-45ca-91e0-34e315f5bee2", "name": "numerai", "tournament": 8, "active": true},
      {"id": "1adb7bf1-f61a-4718-a73b-fd516e32a475", "name": "signals", "tournament": 11, "active": true},
      {"id": "31fec939-52ec-4558-ab44-678dd2822b15", "name": "crypto", "tournament": 12, "active": true}
    ]
  }
}
```

**Tournament IDs:**
- **8**: Classic Numerai Tournament
- **11**: Numerai Signals
- **12**: Crypto Signals

## Core Queries

### 1. Tournaments Query
Get tournament information and rounds.

**Query:**
```graphql
{
  tournaments {
    id
    name
    tournament
    active
    rounds {
      number
      openTime
      closeTime
      resolvedGeneral
    }
  }
}
```

**Parameters:**
- None required

### 2. Rounds Query
Get round information with filtering options.

**Query:**
```graphql
{
  rounds(tournament: 8, limit: 5, status: OPEN) {
    number
    openTime
    closeTime
    resolveTime
    scoreTime
    resolvedGeneral
    resolvedStaking
    tournament
    target
    numTickers
    payoutFactor
  }
}
```

**Parameters:**
- `tournament` (Int): Tournament ID (default: varies by query)
- `limit` (Int): Number of results to return
- `number` (Int): Specific round number
- `status` (RoundStatus): Filter by round status
- `target` (String): Target variable filter

**Example:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ rounds(tournament: 8, limit: 3) { number openTime closeTime resolvedGeneral } }"}' \
  https://api-tournament.numer.ai/
```

### 3. Account Query
Get current user account information (requires authentication).

**Query:**
```graphql
{
  account {
    id
    username
    displayName
    email
    availableNmr
    totalStakeValues {
      value
      date
    }
    models {
      id
      name
      tournament
      returns {
        oneDay
        oneWeek
        oneMonth
        threeMonths
        oneYear
        allTime
      }
    }
  }
}
```

### 4. Account Profile Query
Get public profile information for any user.

**Query:**
```graphql
{
  accountProfile(username: "username_here", tournament: 8) {
    id
    username
    displayName
    bio
    location
    models {
      id
      displayName
      tournament
    }
    returns {
      oneDay
      oneWeek
      oneMonth
      threeMonths
      oneYear
      allTime
    }
  }
}
```

**Parameters:**
- `username` (String, required): Username to look up
- `tournament` (Int): Tournament ID (default: 8)

**Important:** The `models` field returns `ModelProfile` objects, which use `displayName` (not `name`) for the model name. See [ModelProfile Type](#modelprofile-type) for all available fields.

### 5. Account Leaderboard Query
Get leaderboard rankings with filtering and sorting.

**Query:**
```graphql
{
  accountLeaderboard(
    tournament: 8,
    limit: 10,
    offset: 0,
    orderBy: "corr",
    direction: "desc"
  ) {
    username
    displayName
    rank
    corr
    corr60
    mmc
    mmc60
    nmrStaked
    return1y
    return3m
    returnAllTime
  }
}
```

**Parameters:**
- `tournament` (Int): Tournament ID (default: 8)
- `limit` (Int): Number of results
- `offset` (Int): Pagination offset
- `orderBy` (String): Sort field
- `direction` (String): "asc" or "desc"
- `filterBy` (String): Filter criteria

### 6. Model Query
Get detailed information about a specific model.

**Query:**
```graphql
{
  model(modelId: "model-id-here") {
    id
    name
    username
    tournament
    description
    computeEnabled
    returns {
      oneDay
      oneWeek
      oneMonth
      threeMonths
      oneYear
      allTime
    }
    returnsValues {
      date
      value
    }
    latestSubmissions {
      id
      filename
      insertedAt
      round {
        number
        tournament
      }
    }
  }
}
```

**Parameters:**
- `modelId` (ID, required): Model UUID

### 7. Submissions Query
Get submission history for a model.

**Query:**
```graphql
{
  submissions(modelId: "model-id-here") {
    id
    filename
    insertedAt
    round {
      number
      openTime
      closeTime
      tournament
    }
    validationCorrelation
    validationMmc
  }
}
```

**Parameters:**
- `modelId` (ID): Model UUID
- `id` (ID): Specific submission ID

### 8. V2 Round Model Performances Query
Get detailed performance metrics for models across rounds.

**Query:**
```graphql
{
  v2RoundModelPerformances(
    modelId: "model-id-here",
    tournament: 8,
    lastNRounds: 20
  ) {
    roundNumber
    corr
    mmc
    fnc
    tc
    corrPercentile
    mmcPercentile
    roundResolved
    selectedStakeValue
    payout
  }
}
```

**Parameters:**
- `modelId` (String): Model UUID
- `tournament` (Int): Tournament ID (default: 8)
- `lastNRounds` (Int): Number of recent rounds
- `roundNumberGte` (Int): Round number greater than or equal
- `roundNumberLte` (Int): Round number less than or equal
- `resolvedOnly` (Boolean): Only resolved rounds
- `submittedOnly` (Boolean): Only rounds with submissions

### 9. Dataset Query
Get information about datasets for download.

**Query:**
```graphql
{
  dataset(tournament: 8, round: 1055, filename: "train.csv") {
    id
    filename
    round {
      number
      tournament
    }
    url
  }
}
```

**Parameters:**
- `tournament` (Int): Tournament ID (default: 8)
- `round` (Int): Round number
- `filename` (String): Specific filename

### 10. List Datasets Query
Get available datasets for a tournament/round.

**Query:**
```graphql
{
  listDatasets(tournament: 8, round: 1055) {
    filename
    url
  }
}
```

### 11. Round Details Query
Get comprehensive details for a specific round, including all model performances, stakes, payouts, and histogram data.

**Query:**
```graphql
query roundDetails($tournament: Int!, $roundNumber: Int!) {
  roundDetails(tournament: $tournament, roundNumber: $roundNumber) {
    # Round metadata
    roundNumber
    roundId
    tournament
    status
    roundTarget
    openTime
    closeTime
    closeStakingTime
    scoresUpdatedTime
    roundResolveTime
    payoutFactor

    # Aggregate statistics
    totalPayout
    totalEarned
    totalBurned
    totalAtStake
    totalStakes

    # Model performances
    models {
      id
      modelName
      profileUrl
      team
      computeEnabled
      selectedStakeValue
      payoutPending
      payoutSettled

      # Common metrics (Numerai & Signals)
      tc
      tcPercentile

      # Numerai-specific metrics
      corrWMetaModel
      fnc
      corr20: corr_20
      v2_corr20: v2Corr20
      corr60: corr_60
      mmc60: mmc_60
      cort20
      fnc_v3: fncV3
      mcwnm
      apcwnm
      mmc
      mmcPercentile
      bmc

      # Signals-specific metrics
      corr
      corr_v4: corrV4
      ric
      fnc_v4: fncV4
      ic_v2: icV2
      cwsnmm
      mcwsm
      apcwsm
      alpha
      mpc
    }

    # Score distribution histograms
    allHistogramData {
      bins
      counts
    }
    stakedHistogramData {
      bins
      counts
    }
  }
}
```

**Parameters:**
- `tournament` (Int!, required): Tournament ID (8 = Numerai, 11 = Signals, 12 = Crypto)
- `roundNumber` (Int!, required): The round number to query

**Example:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "query": "query roundDetails($tournament: Int!, $roundNumber: Int!) { roundDetails(tournament: $tournament, roundNumber: $roundNumber) { roundNumber status openTime closeTime totalAtStake totalPayout payoutFactor models { modelName selectedStakeValue mmc corr60 payoutSettled } } }",
    "variables": {"tournament": 8, "roundNumber": 1170}
  }' \
  https://api-tournament.numer.ai/
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `roundNumber` | Int | Round identifier |
| `status` | String | Round status (e.g., "RESOLVED", "OPEN") |
| `openTime` | DateTime | When round opened for submissions |
| `closeTime` | DateTime | When round closed for submissions |
| `closeStakingTime` | DateTime | Deadline for stake changes |
| `roundResolveTime` | DateTime | When round results are finalized |
| `payoutFactor` | String | Multiplier for payouts this round |
| `totalAtStake` | String | Total NMR staked in the round |
| `totalPayout` | String | Total NMR paid out |
| `totalEarned` | String | Total NMR earned by participants |
| `totalBurned` | String | Total NMR burned |

**Model Performance Fields:**

| Field | Description |
|-------|-------------|
| `corrWMetaModel` | Correlation with the meta model (0-1) |
| `mmc` | Meta Model Contribution |
| `mmc60` | 60-day MMC |
| `corr60` | 60-day correlation |
| `v2_corr20` | V2 20-day correlation |
| `fnc_v3` | Feature Neutral Correlation V3 |
| `mcwnm` | Meta Contribution Weighted by Numerai Meta |
| `apcwnm` | Average Pairwise Correlation Weighted by Numerai Meta |
| `bmc` | Benchmark Meta Contribution |

**Note:** This query returns a large response (~1.5MB compressed for active rounds) as it includes all participating models. Consider fetching only the fields you need.

### 12. Currency Price Query
Get the current exchange rate between NMR and fiat currencies.

**Query:**
```graphql
query latestCurrencyPrice($targetSymbol: String!, $baseSymbol: String!) {
  latestCurrencyPrice(targetSymbol: $targetSymbol, baseSymbol: $baseSymbol) {
    lastUpdated
    baseSymbol
    targetSymbol
    price
  }
}
```

**Parameters:**
- `targetSymbol` (String!, required): Target currency symbol (e.g., "USD", "EUR")
- `baseSymbol` (String!, required): Base currency symbol (e.g., "NMR")

**Example:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "query": "query latestCurrencyPrice($targetSymbol: String!, $baseSymbol: String!) { latestCurrencyPrice(targetSymbol: $targetSymbol, baseSymbol: $baseSymbol) { lastUpdated baseSymbol targetSymbol price } }",
    "variables": {"targetSymbol": "USD", "baseSymbol": "NMR"}
  }' \
  https://api-tournament.numer.ai/
```

**Response:**
```json
{
  "data": {
    "latestCurrencyPrice": {
      "baseSymbol": "NMR",
      "lastUpdated": "2026-01-31 20:18:00Z",
      "price": "9.00260163",
      "targetSymbol": "USD"
    }
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `baseSymbol` | String | The base currency (NMR) |
| `targetSymbol` | String | The target currency (USD) |
| `price` | String | Current exchange rate (1 NMR = X USD) |
| `lastUpdated` | DateTime | When the price was last updated |

**Use Cases:**
- Display NMR values in USD on dashboards
- Calculate fiat equivalent of stakes and payouts
- Track NMR price history

## Key Object Types

### Model Type
```graphql
type Model {
  id: ID
  name: String
  username: String
  tournament: Int
  description: String
  computeEnabled: Boolean
  hidden: Boolean
  returns: Returns
  returnsValues: [ReturnsValue]
  latestSubmissions: [LatestSubmission]
  v2Stake: V2Stake
  submissionWebhook: String
}
```

**Note:** This type is returned by the `model(modelId)` query and `account.models`. For models returned by `accountProfile.models`, see [ModelProfile Type](#modelprofile-type) below.

### ModelProfile Type
This type is returned when querying models via `accountProfile`. It has different fields than the `Model` type.

```graphql
type ModelProfile {
  id: ID
  displayName: String          # Use this instead of "name"
  tournament: Int
  username: String
  accountId: ID
  profileUrl: String
  startDate: Time
  stake: Nmr
  return1y: Float
  # Reputation scores
  corrRep: Float
  corr60Rep: Float
  corr20V2Rep: Float
  corrV4Rep: Float
  corj60Rep: Float
  mmcRep: Float
  mmc60Rep: Float
  tcRep: Float
  fncV3Rep: Float
  fncV4Rep: Float
  icV2Rep: Float
  ricRep: Float
  mpcRep: Float
  alphaRep: Float
}
```

**Important:** When querying `accountProfile.models`, use `displayName` to get the model name, not `name`. The `name` field does not exist on `ModelProfile`.

**Example:**
```graphql
{
  accountProfile(username: "videigren", tournament: 8) {
    models {
      id
      displayName
      tournament
    }
  }
}
```

**Response:**
```json
{
  "data": {
    "accountProfile": {
      "models": [
        {"id": "97b8045c-77b5-47bf-bfb1-76bf3d785d6e", "displayName": "videigren", "tournament": 8}
      ]
    }
  }
}
```

### Round Type
```graphql
type Round {
  id: ID
  number: Int
  tournament: Int
  openTime: Time
  closeTime: Time
  resolveTime: Time
  scoreTime: Time
  resolvedGeneral: Boolean
  resolvedStaking: Boolean
  target: String
  numTickers: Int
  payoutFactor: String
  stakeThreshold: Float
}
```

### Account Type
```graphql
type Account {
  id: ID
  username: String
  displayName: String
  email: String
  availableNmr: Nmr
  models: [Model]
  returns: SwReturns
  totalStakeValues: [StakeValue]
  achievements: [Achievement]
  apiTokens: [ApiToken]
}
```

### Tournament Type
```graphql
type Tournament {
  id: ID
  name: String
  tournament: Int
  active: Boolean
  rounds: [Round]
}
```

## Common Query Examples

### Get Current Round Information
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ rounds(tournament: 8, limit: 1) { number openTime closeTime resolvedGeneral } }"}' \
  https://api-tournament.numer.ai/
```

### Get Top 10 Leaderboard
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountLeaderboard(tournament: 8, limit: 10, orderBy: \"corr\", direction: \"desc\") { username rank corr mmc nmrStaked } }"}' \
  https://api-tournament.numer.ai/
```

### Get Model Performance History
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ v2RoundModelPerformances(modelId: \"your-model-id\", lastNRounds: 10) { roundNumber corr mmc payout } }"}' \
  https://api-tournament.numer.ai/
```

### Get User Profile
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountProfile(username: \"username\", tournament: 8) { displayName bio models { id displayName tournament } returns { oneYear allTime } } }"}' \
  https://api-tournament.numer.ai/
```

## Available Mutations

The API also supports mutations for authenticated operations like:
- `addModel`: Create a new model
- `stake`: Stake NMR on a model
- `unstake`: Remove NMR stake
- `submit`: Submit predictions
- `updateModel`: Update model settings

## Error Handling

GraphQL errors are returned in the response under the `errors` field:

```json
{
  "errors": [
    {
      "message": "Error description",
      "locations": [{"line": 1, "column": 1}],
      "path": ["fieldName"]
    }
  ],
  "data": null
}
```

## Rate Limiting

The API implements rate limiting. Be respectful with request frequency to avoid being throttled.

## Tips for Usage

1. **Use field selection**: Only request the fields you need to minimize response size
2. **Pagination**: Use `limit` and `offset` parameters for large datasets
3. **Filtering**: Use available filter parameters to get specific data
4. **Introspection**: Use schema introspection to discover new fields and types
5. **Error handling**: Always check for errors in the response
6. **Model vs ModelProfile**: The `accountProfile.models` field returns `ModelProfile` objects (use `displayName`), while `account.models` and `model()` query return `Model` objects (use `name`). This is a common source of errors.

## Crypto Tournament API Differences

The Crypto Signals tournament (ID: 12) has some key differences from the Classic tournament (ID: 8) when querying the API.

### Key Differences

| Feature | Classic (Tournament 8) | Crypto (Tournament 12) |
|---------|------------------------|------------------------|
| Model lookup | `v3UserProfile(modelName: "model_name")` | Use `accountProfile` with `tournament: 12` |
| Performance data | `v3UserProfile.roundModelPerformances` | `v2RoundModelPerformances(modelId: UUID, tournament: 12)` |
| Model identifier | Model name (string) | Model UUID |
| Score fields | Direct fields (corr, mmc, etc.) | Nested in `submissionScores` array |

### Getting Crypto Models for a User

To get a user's Crypto tournament models, you MUST include the `tournament` parameter:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountProfile(username: \"fish_n_chips\", tournament: 12) { username models { id displayName tournament } } }"}' \
  https://api-tournament.numer.ai/
```

**Response:**
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

**Important:** Without the `tournament: 12` parameter, `accountProfile` returns Classic (tournament 8) models only.

### Getting Crypto Model Performance Data

Crypto models use `v2RoundModelPerformances` instead of `v3UserProfile.roundModelPerformances`:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ v2RoundModelPerformances(modelId: \"b27db79e-bafa-4a76-8a75-9f91168cd222\", tournament: 12, lastNRounds: 10) { roundNumber roundResolved submissionScores { displayName value } } }"}' \
  https://api-tournament.numer.ai/
```

**Response:**
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

### Crypto Leaderboard

To get the Crypto tournament leaderboard:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "{ accountLeaderboard(tournament: 12, limit: 10) { username rank corr mmc nmrStaked } }"}' \
  https://api-tournament.numer.ai/
```

### Available Score Types in Crypto

The `submissionScores` array contains these metrics for Crypto:

| displayName | Description |
|-------------|-------------|
| `corr` | Correlation score |
| `mmc` | Meta Model Contribution |
| `canon_corr` | Canonical correlation |
| `canon_mmc` | Canonical MMC |
| `apcwcm` | Average pairwise correlation weighted by crypto market cap |
| `mcwcm` | Market cap weighted correlation metric |
| `season_score` | Current season score |

### Workflow for Crypto Tournament

1. **Find user models** - Use `accountProfile(username, tournament: 12)` to get model list with UUIDs
2. **Get model ID** - Extract the `id` field (UUID) from the model
3. **Fetch performance** - Use `v2RoundModelPerformances(modelId: UUID, tournament: 12)` for metrics
4. **Access scores** - Parse the `submissionScores` array for individual metrics

### Example: Complete Workflow

```javascript
// Step 1: Get user's Crypto models
const modelsQuery = `{
  accountProfile(username: "fish_n_chips", tournament: 12) {
    models { id displayName tournament }
  }
}`;

// Step 2: Use model UUID to get performance
const modelId = "b27db79e-bafa-4a76-8a75-9f91168cd222"; // fncc_t1
const perfQuery = `{
  v2RoundModelPerformances(modelId: "${modelId}", tournament: 12, lastNRounds: 20) {
    roundNumber
    roundResolved
    submissionScores { displayName value }
  }
}`;

// Step 3: Extract corr and mmc from submissionScores
const corr = submissionScores.find(s => s.displayName === 'corr')?.value;
const mmc = submissionScores.find(s => s.displayName === 'mmc')?.value;
```

## Intra-Round Performance Data (Daily Scores)

The Numerai platform provides daily performance updates during each round via the `v2RoundModelPerformances` query with the `intraRoundSubmissionScores` field. This allows you to track how your model is performing day-by-day as the round progresses.

### Query Structure

```graphql
query v2IntraRoundModelPerformances(
  $modelId: String!,
  $roundNumber__eq: Int,
  $roundNumber__gte: Int,
  $tournament: Int,
  $distinctOnRound: Boolean
) {
  v2RoundModelPerformances(
    modelId: $modelId,
    roundNumber__eq: $roundNumber__eq,
    roundNumber__gte: $roundNumber__gte,
    distinctOnRound: $distinctOnRound,
    tournament: $tournament
  ) {
    roundNumber
    roundResolveTime
    roundPayoutFactor
    roundScoreTime
    roundResolved
    roundTarget
    atRisk
    corrMultiplier
    mmcMultiplier
    tcMultiplier
    intraRoundSubmissionScores {
      displayName
      value
      percentile
      day
      date
      payoutPending
      payoutSettled
    }
  }
}
```

### Parameters

- `modelId` (String, required): Model UUID (not model name)
- `roundNumber__eq` (Int): Get data for a specific round number
- `roundNumber__gte` (Int): Get data for rounds greater than or equal to this number
- `tournament` (Int): Tournament ID (default: 8)
- `distinctOnRound` (Boolean): Return only one entry per round (set to false for intra-round data)

### Usage Examples

#### Get Daily Performance for Specific Round

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "query": "query v2IntraRoundModelPerformances($modelId: String!, $roundNumber__eq: Int, $tournament: Int) { v2RoundModelPerformances(modelId: $modelId, roundNumber__eq: $roundNumber__eq, tournament: $tournament) { roundNumber roundResolved atRisk intraRoundSubmissionScores { displayName value percentile day date payoutPending payoutSettled } } }",
    "variables": {
      "modelId": "5007889e-7286-4f2a-a5ed-d213f0a47d47",
      "roundNumber__eq": 1166,
      "tournament": 8
    }
  }' \
  https://api-tournament.numer.ai/
```

#### Get All Unresolved Rounds for a Model

To get all unresolved rounds, first query for rounds where `resolvedGeneral` is false, then fetch their intra-round data:

```bash
# Step 1: Get current unresolved rounds
curl -X POST -H "Content-Type: application-json" \
  -d '{
    "query": "{ rounds(tournament: 8, status: RESOLVING) { number } }"
  }' \
  https://api-tournament.numer.ai/

# Step 2: For each round, fetch intra-round performance data using the query above
```

### Response Structure

The `intraRoundSubmissionScores` field returns an array of daily scores. Each entry contains:

- **date** (String): ISO 8601 date (e.g., "2026-01-23T00:00:00Z")
- **day** (Int): Day number within the round (1 = first day)
- **displayName** (String): Metric name (see available metrics below)
- **value** (Float): The score value for this metric
- **percentile** (Float): Percentile rank (0-1) compared to all submissions
- **payoutPending** (String): Pending payout amount in NMR
- **payoutSettled** (String): Settled payout amount in NMR

### Available Metrics in intraRoundSubmissionScores

The daily performance data includes multiple metrics tracked separately. Common metrics include:

| displayName | Description |
|-------------|-------------|
| `mmc20` | Meta Model Contribution (20-day) |
| `corr20` | Correlation (20-day) |
| `mmc60` | Meta Model Contribution (60-day) |
| `corr60` | Correlation (60-day) |
| `apcwnm` | Average Pairwise Correlation Weighted by Numerai Meta |
| `mcwnm` | Meta Contribution Weighted by Numerai Meta |
| `bmc` | Benchmark Meta Contribution |
| `canon_corr` | Canonical correlation |
| `canon_mmc` | Canonical MMC |
| `canon_bmc` | Canonical BMC |
| `fnc` | Feature Neutral Correlation |
| `tc` | True Contribution |

### Data Organization

**Important**: The response contains **multiple entries per day** - one for each metric. To get a complete picture for a specific day:

1. Filter `intraRoundSubmissionScores` by `day` value
2. Extract each metric by its `displayName`
3. Build a complete row with all metrics for that day

### Example Response

```json
{
  "data": {
    "v2RoundModelPerformances": [
      {
        "roundNumber": 1166,
        "roundResolved": false,
        "atRisk": "0.000000000000000000",
        "corrMultiplier": 0.75,
        "mmcMultiplier": 2.25,
        "intraRoundSubmissionScores": [
          {
            "date": "2026-01-23T00:00:00Z",
            "day": 19,
            "displayName": "mmc20",
            "value": -0.0111,
            "percentile": 0.2188,
            "payoutPending": "0.000000000000000000",
            "payoutSettled": "0.000000000000000000"
          },
          {
            "date": "2026-01-23T00:00:00Z",
            "day": 19,
            "displayName": "corr20",
            "value": -0.020,
            "percentile": 0.1350,
            "payoutPending": "0.000000000000000000",
            "payoutSettled": "0.000000000000000000"
          },
          {
            "date": "2026-01-23T00:00:00Z",
            "day": 19,
            "displayName": "mmc60",
            "value": -0.0111,
            "percentile": 0.2188,
            "payoutPending": "0.000000000000000000",
            "payoutSettled": "0.000000000000000000"
          },
          {
            "date": "2026-01-23T00:00:00Z",
            "day": 19,
            "displayName": "corr60",
            "value": -0.020,
            "percentile": 0.1350,
            "payoutPending": "0.000000000000000000",
            "payoutSettled": "0.000000000000000000"
          }
        ]
      }
    ]
  }
}
```

### Complete Workflow Example

```python
import httpx

# Step 1: Get model ID for a user
query_user = """
{
  accountProfile(username: "gbrecht22", tournament: 8) {
    models { id displayName }
  }
}
"""

# Step 2: Get daily performance data
model_id = "5007889e-7286-4f2a-a5ed-d213f0a47d47"
query_performance = """
query v2IntraRoundModelPerformances($modelId: String!, $roundNumber__eq: Int) {
  v2RoundModelPerformances(
    modelId: $modelId,
    roundNumber__eq: $roundNumber__eq,
    tournament: 8
  ) {
    roundNumber
    roundResolved
    intraRoundSubmissionScores {
      date
      day
      displayName
      value
      percentile
      payoutPending
      payoutSettled
    }
  }
}
"""

variables = {
    "modelId": model_id,
    "roundNumber__eq": 1166
}

response = httpx.post(
    "https://api-tournament.numer.ai/",
    json={"query": query_performance, "variables": variables}
)

# Step 3: Parse the daily scores
data = response.json()["data"]["v2RoundModelPerformances"][0]
scores_by_day = {}

for score in data["intraRoundSubmissionScores"]:
    day = score["day"]
    if day not in scores_by_day:
        scores_by_day[day] = {"date": score["date"], "day": day}

    # Add metric to the day's data
    metric_name = score["displayName"]
    scores_by_day[day][f"{metric_name}_value"] = score["value"]
    scores_by_day[day][f"{metric_name}_percentile"] = score["percentile"]

# Now scores_by_day contains one entry per day with all metrics
```

### Use Cases

1. **Daily Monitoring**: Track model performance as the round progresses
2. **Historical Analysis**: Analyze how models performed during specific market conditions
3. **Performance Attribution**: Compare different metrics (MMC vs CORR) day-by-day
4. **Payout Projections**: Use `payoutPending` to estimate upcoming payouts

### Notes

- Daily scores update once per day as new market data becomes available
- Not all metrics may be available for all days (newer metrics may not have historical data)
- The `roundResolved` field indicates whether the round has finished
- Use `atRisk` to see how much NMR stake is at risk for this round
- Multipliers (`corrMultiplier`, `mmcMultiplier`) show the payout weights for this round

## Additional Resources

- [Numerai Documentation](https://docs.numer.ai/)
- [GraphQL Specification](https://graphql.org/learn/)
- [NumerAPI Python Client](https://github.com/numerai/numerapi)