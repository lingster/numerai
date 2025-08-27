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
      name
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
  -d '{"query": "{ accountProfile(username: \"username\") { displayName bio models { name tournament } returns { oneYear allTime } } }"}' \
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

## Additional Resources

- [Numerai Documentation](https://docs.numer.ai/)
- [GraphQL Specification](https://graphql.org/learn/)
- [NumerAPI Python Client](https://github.com/numerai/numerapi)