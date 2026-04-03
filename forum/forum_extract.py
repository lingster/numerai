from pathlib import Path
from typing import Optional

import typer
from loguru import logger

from forum_client import DiscourseClient
from forum_converter import write_topic
from forum_index import build_index
from forum_models import CategoryData, ScraperState, TopicData
from forum_state import load_state, needs_update, record_topic, save_state, stamp_run

app = typer.Typer(help="Scrape Numerai forum to markdown files.")


def _fetch_topic(
    client: DiscourseClient,
    meta: dict,
    category: CategoryData,
    output_dir: Path,
) -> Optional[TopicData]:
    topic_id = meta["id"]
    try:
        raw, posts = client.get_topic_posts(topic_id)
        topic = TopicData(
            id=raw["id"],
            title=raw["title"],
            slug=raw["slug"],
            category_id=category.id,
            category_name=category.name,
            category_slug=category.slug,
            created_at=raw["created_at"],
            last_posted_at=raw["last_posted_at"],
            posts_count=raw["posts_count"],
            views=raw["views"],
            like_count=raw.get("like_count", 0),
            tags=raw.get("tags", []),
            posts=posts,
        )
        write_topic(output_dir, topic)
        return topic
    except Exception as exc:
        logger.error(f"Failed topic {topic_id} ({meta.get('slug', '?')}): {exc}")
        return None


@app.command()
def scrape(
    output: Path = typer.Option(Path("./output"), "--output", "-o", help="Output directory"),
    full_refresh: bool = typer.Option(False, "--full-refresh", "-f", help="Re-fetch all topics"),
    delay: float = typer.Option(0.5, "--delay", "-d", help="Seconds between API requests"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Debug logging"),
) -> None:
    """Scrape the Numerai Discourse forum to markdown files with incremental updates."""
    if verbose:
        logger.enable("__main__")

    output.mkdir(parents=True, exist_ok=True)
    state: ScraperState = ScraperState() if full_refresh else load_state(output)

    fetched = skipped = errors = 0
    seen_ids: set[int] = set()

    with DiscourseClient(delay=delay) as client:
        categories = client.get_categories()
        logger.info(f"Found {len(categories)} categories")

        for category in categories:
            logger.info(f"Category: {category.name} ({category.topic_count} topics)")
            page = 0

            while True:
                topic_metas, has_more = client.get_category_topics(category.slug, page)

                for meta in topic_metas:
                    tid = meta["id"]
                    if tid in seen_ids:
                        continue  # skip pinned duplicates across pages
                    seen_ids.add(tid)

                    last_posted = meta.get("last_posted_at") or meta["created_at"]
                    count = meta.get("posts_count", 1)

                    if not full_refresh and not needs_update(state, tid, last_posted, count):
                        skipped += 1
                        continue

                    topic = _fetch_topic(client, meta, category, output)
                    if topic:
                        record_topic(state, topic)
                        fetched += 1
                        logger.info(f"  [{fetched}] {topic.title[:60]}")
                    else:
                        errors += 1

                if not has_more:
                    break
                page += 1

        build_index(output, state, categories)
        stamp_run(state)
        save_state(output, state)

    logger.info(f"Complete — fetched: {fetched}, skipped: {skipped}, errors: {errors}")
    typer.echo(f"Done. {fetched} fetched, {skipped} up-to-date, {errors} errors → {output}/")


if __name__ == "__main__":
    app()
