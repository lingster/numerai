from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostData(BaseModel):
    id: int
    post_number: int
    username: str
    created_at: datetime
    cooked: str  # HTML content
    reply_to_post_number: Optional[int] = None
    like_count: int = 0


class TopicData(BaseModel):
    id: int
    title: str
    slug: str
    category_id: int
    category_name: str
    category_slug: str
    created_at: datetime
    last_posted_at: datetime
    posts_count: int
    views: int
    like_count: int = 0
    tags: list[str] = []
    posts: list[PostData] = []


class CategoryData(BaseModel):
    id: int
    name: str
    slug: str
    topic_count: int
    description: str = ""


class TopicState(BaseModel):
    """Lightweight record stored in state for index rebuilding."""
    last_posted_at: str
    posts_count: int
    slug: str
    category_slug: str
    category_name: str
    title: str
    views: int
    file_path: str


class ScraperState(BaseModel):
    last_run_at: Optional[str] = None
    topics: dict[str, TopicState] = {}  # keyed by str(topic_id)
