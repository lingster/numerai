from datetime import datetime
from pathlib import Path

import html2text
from loguru import logger

from forum_models import TopicData

BASE_URL = "https://forum.numer.ai"


def _make_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # no forced line wrapping
    h.protect_links = True
    h.unicode_snob = True
    return h


def _html_to_md(html: str) -> str:
    return _make_converter().handle(html).strip()


def _fmt_dt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M UTC")


def _frontmatter(topic: TopicData) -> str:
    title_safe = topic.title.replace('"', "'")
    tags_str = f"[{', '.join(topic.tags)}]" if topic.tags else "[]"
    return (
        "---\n"
        f'title: "{title_safe}"\n'
        f"category: {topic.category_name}\n"
        f"url: {BASE_URL}/t/{topic.slug}/{topic.id}\n"
        f"created_at: {topic.created_at.isoformat()}\n"
        f"last_posted_at: {topic.last_posted_at.isoformat()}\n"
        f"posts_count: {topic.posts_count}\n"
        f"views: {topic.views}\n"
        f"tags: {tags_str}\n"
        "---\n"
    )


def topic_to_markdown(topic: TopicData) -> str:
    parts = [_frontmatter(topic), f"# {topic.title}\n"]

    for post in topic.posts:
        reply_note = (
            f" _(reply to #{post.reply_to_post_number})_"
            if post.reply_to_post_number
            else ""
        )
        header = (
            f"### Post #{post.post_number} — **{post.username}**"
            f" | {_fmt_dt(post.created_at)}{reply_note}"
        )
        body = _html_to_md(post.cooked) if post.cooked else "_[no content]_"
        parts.append(f"---\n\n{header}\n\n{body}\n")

    return "\n".join(parts)


def write_topic(output_dir: Path, topic: TopicData) -> Path:
    dest = output_dir / topic.category_slug / f"{topic.slug}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(topic_to_markdown(topic), encoding="utf-8")
    logger.debug(f"Written: {dest}")
    return dest
