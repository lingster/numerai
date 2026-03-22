# numerai-ql

A Claude Code plugin for querying the [Numerai Tournament GraphQL API](https://api-tournament.numer.ai/).

## What It Does

The `numerai-ql` skill lets you ask Claude natural language questions about Numerai tournament data. Claude will query the GraphQL API and present results in a readable format.

## Example Queries

```
"What's the current round number for the Numerai tournament?"
"Show me the top 10 models on the Numerai leaderboard"
"Get the performance history for user 'videigren'"
"What is the NMR price in USD?"
"Show me daily scores for my model in the last round"
"Get corr and mmc scores for model UUID abc-123 in the last 20 rounds"
"Show me the Crypto tournament leaderboard"
```

## Tournaments

| ID | Name | Description |
|----|------|-------------|
| 8 | numerai | Classic Numerai Tournament |
| 11 | signals | Numerai Signals |
| 12 | crypto | Crypto Signals |

## Installation

From a marketplace that hosts this plugin, install with:

```
/plugin install numerai-ql
```

Or install locally:

```bash
# Point Claude Code at this directory
cc --plugin-dir /path/to/numerai-ql
```

## Skill Structure

```
numerai-ql/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── numerai-ql/
│       ├── SKILL.md                         # Core skill instructions
│       ├── references/
│       │   ├── api-reference.md             # Full query reference
│       │   ├── crypto-tournament.md         # Crypto-specific patterns
│       │   └── intra-round.md              # Daily score queries
│       ├── examples/
│       │   ├── get_model_performance.py     # Python CLI tool
│       │   └── leaderboard_query.sh        # Shell query examples
│       └── scripts/
│           └── query.sh                    # Reusable curl wrapper
└── README.md
```

## Using the Example Scripts

```bash
# Query the API directly (requires bash + curl)
cd skills/numerai-ql/scripts
./query.sh '{ rounds(tournament: 8, limit: 1) { number openTime closeTime } }'

# Get model performance with Python
cd skills/numerai-ql/examples
pip install httpx
python get_model_performance.py --username myuser --rounds 20

# Shell examples
bash leaderboard_query.sh
```

## API Endpoint

All queries go to: `https://api-tournament.numer.ai/`

Most queries are public and require no authentication.
