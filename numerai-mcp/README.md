# Numerai MCP Server

Python MCP server that exposes common Numerai GraphQL queries as tools.

## Setup

```bash
cd numerai-mcp
python3 -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]" httpx
```

## Standalone Run

```bash
python numerai_mcp.py
```

## Auth (optional)

Set these environment variables for authenticated queries:

```bash
export NUMERAI_PUBLIC_ID="your_public_id"
export NUMERAI_SECRET_KEY="your_secret_key"
```

## Integration

### Claude Code (CLI)

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "numerai-graphql": {
      "command": "/absolute/path/to/numerai-mcp/.venv/bin/python",
      "args": [
        "/absolute/path/to/numerai-mcp/numerai_mcp.py"
      ],
      "env": {
        "NUMERAI_PUBLIC_ID": "your_public_id_here",
        "NUMERAI_SECRET_KEY": "your_secret_key_here"
      }
    }
  }
}
```

**Notes:**
- Use absolute paths to the virtual environment's Python interpreter
- Add your API credentials in the `env` section (or leave empty for public queries only)
- Restart Claude Code after updating settings
- Test with commands like asking Claude to "list numerai tournaments" or "get current round info"

### Claude for Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "numerai-graphql": {
      "command": "/absolute/path/to/numerai-mcp/.venv/bin/python",
      "args": [
        "/absolute/path/to/numerai-mcp/numerai_mcp.py"
      ],
      "env": {
        "NUMERAI_PUBLIC_ID": "your_public_id_here",
        "NUMERAI_SECRET_KEY": "your_secret_key_here"
      }
    }
  }
}
```

## Available Tools

The server exposes 15 MCP tools:

- `auth_status()` - Check API credential configuration
- `list_tournaments()` - Get all tournaments
- `rounds()` - Query rounds with filtering
- `account()` - Get authenticated account details (requires auth)
- `account_profile()` - Public user profiles
- `account_leaderboard()` - Rankings with sorting
- `model()` - Model details and performance
- `submissions()` - Submission history
- `v2_round_model_performances()` - Performance metrics across rounds
- `dataset()` - Dataset download URLs
- `list_datasets()` - Available datasets for a round
- `latest_currency_price()` - NMR currency prices
- `round_details()` - Detailed round data with optional models/histograms
- `graphql_query()` - Execute arbitrary GraphQL queries
