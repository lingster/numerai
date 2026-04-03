# Numerai Forum Scraper

Scrapes the [Numerai Discourse forum](https://forum.numer.ai/) to a collection of markdown files, suitable for use as an LLM knowledge base. Supports incremental daily updates — only topics that have changed since the last run are re-fetched.

## Quick start

```bash
# First run — full scrape (~6,700 posts, ~45 min at default rate limit)
uv run python forum_extract.py --output ./output

# Subsequent runs — incremental, only fetches new/updated topics
uv run python forum_extract.py --output ./output

# Force re-fetch everything
uv run python forum_extract.py --output ./output --full-refresh
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--output` / `-o` | `./output` | Directory to write markdown files |
| `--full-refresh` / `-f` | off | Ignore state, re-fetch all topics |
| `--delay` / `-d` | `0.5` | Seconds between API requests (be polite) |
| `--verbose` / `-v` | off | Enable debug logging |

## Output structure

```
output/
├── index.md                         ← one line per topic across all categories
├── .scraper_state.json              ← incremental state (last_posted_at per topic)
├── announcements/
│   ├── welcome-to-the-numerai-forums.md
│   └── ...
├── data-science/
│   └── ...
├── signals/
├── tournament/
├── feedback/
├── council-of-elders/
├── numeraire/
└── ...
```

### index.md format

```markdown
# Numerai Forum Index
_Last updated: 2026-04-03 15:46 UTC_

_312 topics across 9 categories_

## Announcements

- [Welcome to the Numerai forums](announcements/welcome-to-the-numerai-forums.md) — 2022-12-26 | 1 reply | 12,074 views
```

### Topic file format

Each topic is saved as a markdown file with YAML frontmatter followed by all posts in thread order:

```markdown
---
title: "Topic title"
category: Data Science
url: https://forum.numer.ai/t/topic-slug/123
created_at: 2024-01-10T12:00:00+00:00
last_posted_at: 2024-03-15T08:00:00+00:00
posts_count: 42
views: 5678
tags: []
---

# Topic title

---

### Post #1 — **username** | 2024-01-10 12:00 UTC

Post content...

---

### Post #2 — **username2** | 2024-01-11 09:30 UTC _(reply to #1)_

Reply content...
```

## Daily cron

```bash
# Edit crontab: crontab -e
0 6 * * * cd /path/to/forum && uv run python forum_extract.py --output ./output >> /tmp/forum_scraper.log 2>&1
```

## How it works

The forum runs [Discourse](https://www.discourse.org/), which exposes a public JSON API — no authentication required.

**Incremental updates:** On each run the scraper compares each topic's `last_posted_at` timestamp and `posts_count` against the saved state. Only topics that differ are re-fetched.

**Pagination:** Discourse returns posts in chunks of 20. For topics with more than 20 posts the scraper fetches the remaining post IDs via `/t/{id}/posts.json`.

## Modules

| File | Responsibility |
|------|---------------|
| `forum_extract.py` | CLI entry point (Typer), orchestrates the full scrape |
| `forum_client.py` | Discourse REST API client — categories, topic lists, posts |
| `forum_converter.py` | Converts HTML post content to markdown, writes `.md` files |
| `forum_models.py` | Pydantic v2 models: `PostData`, `TopicData`, `CategoryData`, `ScraperState` |
| `forum_state.py` | Loads/saves `.scraper_state.json`, determines what needs updating |
| `forum_index.py` | Rebuilds `index.md` from the full state after each run |
