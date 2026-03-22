# Numerai GraphQL API Reference

## Endpoint

```
POST https://api-tournament.numer.ai/
Content-Type: application/json
Body: {"query": "...", "variables": {...}}
```

## Tournament IDs

| ID | Name | Description |
|----|------|-------------|
| 8 | numerai | Classic Numerai Tournament |
| 11 | signals | Numerai Signals |
| 12 | crypto | Crypto Signals |

---

## Queries

### `tournaments`

Get all available tournaments.

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

---

### `rounds`

Get round information with filtering.

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| `tournament` | Int | Tournament ID (default: 8) |
| `limit` | Int | Max results |
| `number` | Int | Specific round number |
| `status` | RoundStatus | OPEN, RESOLVING, RESOLVED |
| `target` | String | Target variable filter |

**Fields:**
```graphql
{
  rounds(tournament: 8, limit: 5) {
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

---

### `accountProfile`

Get public profile info for any user. Returns `ModelProfile` objects (use `displayName` not `name`).

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `username` | String | Yes | Username to look up |
| `tournament` | Int | No | Default: 8 |

**Fields:**
```graphql
{
  accountProfile(username: "someuser", tournament: 8) {
    id
    username
    displayName
    bio
    location
    models {
      id
      displayName        # Use this, NOT name
      tournament
      profileUrl
      startDate
      stake
      return1y
      corrRep
      corr60Rep
      mmcRep
      mmc60Rep
      tcRep
      fncV3Rep
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

---

### `accountLeaderboard`

Get leaderboard rankings.

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| `tournament` | Int | Tournament ID (default: 8) |
| `limit` | Int | Number of results |
| `offset` | Int | Pagination offset |
| `orderBy` | String | Sort field (e.g. "corr", "mmc", "nmrStaked") |
| `direction` | String | "asc" or "desc" |
| `filterBy` | String | Filter criteria |

**Fields:**
```graphql
{
  accountLeaderboard(tournament: 8, limit: 10, orderBy: "corr", direction: "desc") {
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

---

### `model`

Get detailed info about a specific model by UUID.

**Parameters:**
| Name | Type | Required |
|------|------|----------|
| `modelId` | ID | Yes |

**Fields:**
```graphql
{
  model(modelId: "uuid-here") {
    id
    name
    username
    tournament
    description
    computeEnabled
    hidden
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
    v2Stake {
      status
      confidence
      value
      txHash
    }
  }
}
```

---

### `v2RoundModelPerformances`

Get performance metrics per round for a model. This is the primary query for model scores.

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| `modelId` | String | Model UUID |
| `tournament` | Int | Tournament ID (default: 8) |
| `lastNRounds` | Int | Number of recent rounds |
| `roundNumberGte` | Int | Round >= this number |
| `roundNumberLte` | Int | Round <= this number |
| `roundNumber__eq` | Int | Specific round |
| `resolvedOnly` | Boolean | Only resolved rounds |
| `submittedOnly` | Boolean | Only rounds with submissions |
| `distinctOnRound` | Boolean | One entry per round |

**Classic Tournament Fields:**
```graphql
{
  v2RoundModelPerformances(modelId: "uuid", tournament: 8, lastNRounds: 20) {
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
    roundResolveTime
    roundPayoutFactor
    roundScoreTime
    roundTarget
    atRisk
    corrMultiplier
    mmcMultiplier
    tcMultiplier
  }
}
```

**With Intra-Round Daily Scores:**
```graphql
{
  v2RoundModelPerformances(modelId: "uuid", roundNumber__eq: 1170, tournament: 8) {
    roundNumber
    roundResolved
    atRisk
    corrMultiplier
    mmcMultiplier
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

**Crypto Tournament Fields** (uses `submissionScores` array):
```graphql
{
  v2RoundModelPerformances(modelId: "uuid", tournament: 12, lastNRounds: 10) {
    roundNumber
    roundResolved
    submissionScores {
      displayName    # "corr", "mmc", "canon_corr", "canon_mmc", "season_score"
      value
    }
  }
}
```

---

### `submissions`

Get submission history for a model.

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| `modelId` | ID | Model UUID |
| `id` | ID | Specific submission ID |

```graphql
{
  submissions(modelId: "uuid") {
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

---

### `roundDetails`

Get comprehensive data for a specific round including all model performances.

**Note**: Response can be ~1.5MB. Fetch only needed fields.

**Parameters:**
| Name | Type | Required |
|------|------|----------|
| `tournament` | Int! | Yes |
| `roundNumber` | Int! | Yes |

```graphql
query roundDetails($tournament: Int!, $roundNumber: Int!) {
  roundDetails(tournament: $tournament, roundNumber: $roundNumber) {
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
    totalPayout
    totalEarned
    totalBurned
    totalAtStake
    totalStakes
    models {
      id
      modelName
      profileUrl
      team
      computeEnabled
      selectedStakeValue
      payoutPending
      payoutSettled
      tc
      tcPercentile
      mmc
      mmcPercentile
      corrWMetaModel
      fnc
      corr20: corr_20
      v2_corr20: v2Corr20
      corr60: corr_60
      mmc60: mmc_60
      bmc
    }
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

**Variables:** `{"tournament": 8, "roundNumber": 1170}`

---

### `listDatasets`

List available datasets for a round.

```graphql
{
  listDatasets(tournament: 8, round: 1170) {
    filename
    url
  }
}
```

---

### `dataset`

Get a specific dataset download URL.

```graphql
{
  dataset(tournament: 8, round: 1170, filename: "train.parquet") {
    id
    filename
    url
    round {
      number
      tournament
    }
  }
}
```

---

### `latestCurrencyPrice`

Get NMR exchange rate.

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

**Variables:** `{"targetSymbol": "USD", "baseSymbol": "NMR"}`

---

### `account` (Authenticated)

Get current user's private account data. Requires API token in Authorization header.

```graphql
{
  account {
    id
    username
    displayName
    email
    availableNmr
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
    totalStakeValues {
      value
      date
    }
  }
}
```

---

## Performance Metric Glossary

| Metric | Description |
|--------|-------------|
| `corr` | Correlation with target |
| `corr20` | 20-day rolling correlation |
| `corr60` | 60-day rolling correlation |
| `mmc` | Meta Model Contribution |
| `mmc20` | 20-day rolling MMC |
| `mmc60` | 60-day rolling MMC |
| `fnc` | Feature Neutral Correlation |
| `fncV3` | Feature Neutral Correlation V3 |
| `tc` | True Contribution |
| `bmc` | Benchmark Meta Contribution |
| `corrWMetaModel` | Correlation with the meta model (0-1) |
| `mcwnm` | Meta Contribution Weighted by Numerai Meta |
| `apcwnm` | Average Pairwise Correlation Weighted by Numerai Meta |
| `corrPercentile` | Percentile rank for corr |
| `mmcPercentile` | Percentile rank for mmc |
| `payout` | NMR payout for the round |
| `selectedStakeValue` | NMR staked |
| `atRisk` | NMR at risk of being burned |

## Reputation Score Fields (ModelProfile)

These are rolling reputation scores on the leaderboard:

| Field | Description |
|-------|-------------|
| `corrRep` | Correlation reputation |
| `corr60Rep` | 60-day corr reputation |
| `mmcRep` | MMC reputation |
| `mmc60Rep` | 60-day MMC reputation |
| `tcRep` | TC reputation |
| `fncV3Rep` | FNC V3 reputation |
| `return1y` | 1-year return |
