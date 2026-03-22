# Intra-Round Performance Data (Daily Scores)

The Numerai platform provides daily score updates during each round via `intraRoundSubmissionScores`.

## Query Structure

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

## Parameters

| Name | Type | Description |
|------|------|-------------|
| `modelId` | String | Model UUID (required) |
| `roundNumber__eq` | Int | Specific round |
| `roundNumber__gte` | Int | Rounds >= this number |
| `tournament` | Int | Tournament ID (default: 8) |
| `distinctOnRound` | Boolean | Set false for intra-round data |

## Available Daily Metrics

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

## Response Structure

**Important**: The response has **multiple entries per day** — one per metric.

Each entry:
- `date` (String): ISO 8601 date, e.g. "2026-01-23T00:00:00Z"
- `day` (Int): Day number within the round (1 = first day)
- `displayName` (String): Metric name
- `value` (Float): Score for this metric
- `percentile` (Float): Percentile rank 0–1 vs all submissions
- `payoutPending` (String): NMR pending payout
- `payoutSettled` (String): NMR settled payout

## Example: Fetch Daily Scores for a Specific Round

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "query": "query { v2RoundModelPerformances(modelId: \"MODEL_UUID\", roundNumber__eq: 1166, tournament: 8) { roundNumber roundResolved atRisk intraRoundSubmissionScores { displayName value percentile day date payoutPending } } }"
  }' \
  https://api-tournament.numer.ai/
```

## Python: Parse Daily Scores into Rows

```python
import httpx

API_URL = "https://api-tournament.numer.ai/"

def get_daily_scores(model_id, round_number, tournament=8):
    query = """
    query($modelId: String!, $roundNumber__eq: Int, $tournament: Int) {
      v2RoundModelPerformances(
        modelId: $modelId,
        roundNumber__eq: $roundNumber__eq,
        tournament: $tournament
      ) {
        roundNumber
        roundResolved
        atRisk
        corrMultiplier
        mmcMultiplier
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
    resp = httpx.post(API_URL, json={
        "query": query,
        "variables": {
            "modelId": model_id,
            "roundNumber__eq": round_number,
            "tournament": tournament
        }
    })
    data = resp.json()["data"]["v2RoundModelPerformances"][0]

    # Pivot: one row per day with all metrics as columns
    scores_by_day = {}
    for score in data["intraRoundSubmissionScores"]:
        day = score["day"]
        if day not in scores_by_day:
            scores_by_day[day] = {"date": score["date"], "day": day}
        metric = score["displayName"]
        scores_by_day[day][f"{metric}_value"] = score["value"]
        scores_by_day[day][f"{metric}_percentile"] = score["percentile"]

    return sorted(scores_by_day.values(), key=lambda r: r["day"])

# Usage
rows = get_daily_scores("5007889e-7286-4f2a-a5ed-d213f0a47d47", 1166)
for row in rows:
    print(f"Day {row['day']} ({row['date'][:10]}): corr20={row.get('corr20_value', 'N/A'):.4f}, mmc20={row.get('mmc20_value', 'N/A'):.4f}")
```

## Notes

- Scores update once per day as new market data arrives
- Not all metrics are available for all days (newer metrics may lack historical data)
- `roundResolved` indicates whether the round has finished
- Use `atRisk` to see NMR stake at risk of being burned
- `corrMultiplier` and `mmcMultiplier` show payout weights for the round
- To monitor all open rounds, first query `rounds(status: RESOLVING)` then fetch intra-round data per round
