# Numerai Claude Code Marketplace

This repository doubles as a [Claude Code plugin marketplace](https://docs.claude.com/en/docs/claude-code/plugins). Users can install the bundled plugins directly from the repo without copying files into `~/.claude` by hand.

## What's published

| Plugin | Type | Purpose |
|--------|------|---------|
| [`numerai-ql`](../numerai-ql) | Skill | Teaches Claude how to query the Numerai GraphQL API (`https://api-tournament.numer.ai/`) — leaderboards, model performance, rounds, intra-round daily scores, NMR price, dataset URLs. |
| [`numerai-mcp`](../numerai-mcp) | MCP server | Python stdio MCP server exposing the same GraphQL queries as typed tools. Auto-registered when the plugin is installed. |

The two plugins are complementary:
- **`numerai-ql`** is lightweight — instructions + curl examples. Works in any Claude Code session with no Python deps.
- **`numerai-mcp`** is heavier — runs a local Python process — but gives Claude typed tool calls and supports authenticated queries.

You can install either, both, or neither.

## Repository layout

```
numerai/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest (lists plugins below)
├── numerai-ql/                   # Plugin: skill
│   ├── .claude-plugin/plugin.json
│   └── skills/numerai-ql/
│       ├── SKILL.md
│       ├── references/
│       ├── examples/
│       └── scripts/
└── numerai-mcp/                  # Plugin: MCP server
    ├── .claude-plugin/plugin.json
    ├── .mcp.json                 # Auto-registers the stdio MCP server
    ├── numerai_mcp.py
    └── pyproject.toml
```

`marketplace.json` references each plugin via a relative `source` path (`./numerai-ql`, `./numerai-mcp`). The marketplace root and the plugin sources live in the same repo, so a single `git clone` (or a single marketplace URL) gives users everything.

## Installation

### From a local clone

```text
/plugin marketplace add /absolute/path/to/numerai
/plugin install numerai-ql@numerai
/plugin install numerai-mcp@numerai
```

The `@numerai` suffix matches the `name` field in `marketplace.json`.

### From GitHub

Once pushed to GitHub:

```text
/plugin marketplace add lingster/numerai
/plugin install numerai-ql@numerai
/plugin install numerai-mcp@numerai
```

### Listing what's available

```text
/plugin marketplace list
/plugin list
```

### Updating

```text
/plugin marketplace update numerai
/plugin update numerai-ql@numerai
```

## How each plugin loads

### `numerai-ql` (skill)

`numerai-ql/.claude-plugin/plugin.json` declares `"skills": ["skills/numerai-ql"]`. When the plugin is installed, Claude Code reads `skills/numerai-ql/SKILL.md` and exposes the skill so Claude will invoke it on relevant prompts ("get model performance", "show leaderboard", etc.).

Nothing runs in the background — the skill is just instructions and example scripts.

### `numerai-mcp` (MCP server)

`numerai-mcp/.mcp.json` looks like this:

```json
{
  "mcpServers": {
    "numerai-graphql": {
      "command": "uv",
      "args": [
        "--directory",
        "${CLAUDE_PLUGIN_ROOT}",
        "run",
        "python",
        "numerai_mcp.py"
      ],
      "env": {}
    }
  }
}
```

When Claude Code starts a session with the plugin enabled, it expands `${CLAUDE_PLUGIN_ROOT}` to the installed plugin directory and runs the command. `uv run` resolves dependencies from the plugin's `pyproject.toml` / `uv.lock` and launches the MCP server over stdio. Claude then sees tools like `list_tournaments`, `account_leaderboard`, `v2_round_model_performances`, etc.

#### Prerequisites

- `uv` must be on `PATH`. Install: `curl -LsSf https://astral.sh/uv/install.sh | sh`.
- Python 3.12+ available to `uv` (it can install one automatically).
- First launch is slow — `uv` materializes a `.venv/` inside the plugin directory and downloads `httpx` + `mcp[cli]`. Subsequent launches are fast.

#### Authentication (optional)

Most Numerai queries are public. For private account data, supply API credentials. There are two places to set them:

1. **Per-user, in Claude Code settings** (preferred — credentials stay out of the marketplace):

   `~/.claude/settings.json`:
   ```json
   {
     "mcpServers": {
       "numerai-graphql": {
         "env": {
           "NUMERAI_PUBLIC_ID": "your_public_id",
           "NUMERAI_SECRET_KEY": "your_secret_key"
         }
       }
     }
   }
   ```
   Claude Code merges this `env` with the plugin's `.mcp.json` at startup.

2. **As shell exports** before launching Claude Code:
   ```bash
   export NUMERAI_PUBLIC_ID=...
   export NUMERAI_SECRET_KEY=...
   ```

The plugin's own `.mcp.json` ships with `env: {}` on purpose — credentials should never be checked in.

## Adding a new plugin to the marketplace

1. Create a directory at the repo root (e.g. `numerai-foo/`).
2. Add `numerai-foo/.claude-plugin/plugin.json` with a `name`, `version`, `description`, and either `"skills": [...]`, `"commands": [...]`, `"agents": [...]`, or `"hooks": {...}` depending on what the plugin ships.
3. If it includes an MCP server, drop a `.mcp.json` at the plugin root.
4. Append an entry to `plugins[]` in `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "numerai-foo",
     "source": "./numerai-foo",
     "description": "...",
     "version": "0.1.0"
   }
   ```
5. Bump the marketplace `metadata.version` if you want users to see "update available" on `/plugin marketplace update`.

## Validating changes

Quick JSON syntax check:

```bash
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
python3 -c "import json; json.load(open('numerai-ql/.claude-plugin/plugin.json'))"
python3 -c "import json; json.load(open('numerai-mcp/.claude-plugin/plugin.json'))"
python3 -c "import json; json.load(open('numerai-mcp/.mcp.json'))"
```

End-to-end smoke test (uses a real Claude Code install):

```bash
# In a throwaway directory
/plugin marketplace add /absolute/path/to/numerai
/plugin install numerai-ql@numerai
# Ask Claude: "what's the current numerai round?"
/plugin install numerai-mcp@numerai
# Restart Claude Code, then ask: "list numerai tournaments via MCP"
```

## References

- Claude Code plugins overview: https://docs.claude.com/en/docs/claude-code/plugins
- Plugin marketplace format: https://docs.claude.com/en/docs/claude-code/plugin-marketplaces
- MCP servers in plugins: https://docs.claude.com/en/docs/claude-code/mcp
- Numerai GraphQL API reference: [`../numerai_graphql.md`](../numerai_graphql.md)
