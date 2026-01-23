# Numerai GraphQL API Documentation

The Numerai Tournament API provides a comprehensive GraphQL endpoint for accessing tournament data, model information, performance metrics, and more.

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

## Additional Resources

- [Numerai Documentation](https://docs.numer.ai/)
- [GraphQL Specification](https://graphql.org/learn/)
- [NumerAPI Python Client](https://github.com/numerai/numerapi)