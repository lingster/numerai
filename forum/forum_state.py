from datetime import datetime, timezone
from pathlib import Path

from loguru import logger

from forum_models import ScraperState, TopicData, TopicState

STATE_FILE = ".scraper_state.json"


def load_state(output_dir: Path) -> ScraperState:
    state_file = output_dir / STATE_FILE
    if state_file.exists():
        return ScraperState.model_validate_json(state_file.read_text())
    return ScraperState()


def save_state(output_dir: Path, state: ScraperState) -> None:
    state_file = output_dir / STATE_FILE
    state_file.write_text(state.model_dump_json(indent=2), encoding="utf-8")
    logger.debug(f"State saved: {state_file}")


def needs_update(state: ScraperState, topic_id: int, last_posted_at: str, posts_count: int) -> bool:
    existing = state.topics.get(str(topic_id))
    if existing is None:
        return True
    return existing.last_posted_at != last_posted_at or existing.posts_count != posts_count


def record_topic(state: ScraperState, topic: TopicData) -> None:
    state.topics[str(topic.id)] = TopicState(
        last_posted_at=topic.last_posted_at.isoformat(),
        posts_count=topic.posts_count,
        slug=topic.slug,
        category_slug=topic.category_slug,
        category_name=topic.category_name,
        title=topic.title,
        views=topic.views,
        file_path=f"{topic.category_slug}/{topic.slug}.md",
    )


def stamp_run(state: ScraperState) -> None:
    state.last_run_at = datetime.now(timezone.utc).isoformat()
