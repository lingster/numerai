from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from loguru import logger

from forum_models import CategoryData, ScraperState

INDEX_FILE = "index.md"


def build_index(output_dir: Path, state: ScraperState, categories: list[CategoryData]) -> None:
    """Rebuild index.md from all entries currently in state."""
    by_category: dict[str, list] = defaultdict(list)
    for topic_state in state.topics.values():
        by_category[topic_state.category_slug].append(topic_state)

    cat_order = {c.slug: i for i, c in enumerate(categories)}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Numerai Forum Index",
        f"_Last updated: {now}_",
        "",
        f"_{sum(len(v) for v in by_category.values())} topics across {len(by_category)} categories_",
        "",
    ]

    for category in sorted(categories, key=lambda c: cat_order.get(c.slug, 999)):
        topics = by_category.get(category.slug, [])
        if not topics:
            continue

        lines.append(f"## {category.name}")
        lines.append("")

        for t in sorted(topics, key=lambda x: x.last_posted_at, reverse=True):
            date_str = t.last_posted_at[:10]  # YYYY-MM-DD from ISO string
            replies = max(0, t.posts_count - 1)
            reply_label = "reply" if replies == 1 else "replies"
            lines.append(
                f"- [{t.title}]({t.file_path})"
                f" — {date_str} | {replies} {reply_label} | {t.views:,} views"
            )

        lines.append("")

    index_path = output_dir / INDEX_FILE
    index_path.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for v in by_category.values())
    logger.info(f"Index written: {index_path} ({total} topics)")
