import time
import httpx
from loguru import logger
from forum_models import PostData, CategoryData

BASE_URL = "https://forum.numer.ai"
CHUNK_SIZE = 20


class DiscourseClient:
    def __init__(self, base_url: str = BASE_URL, delay: float = 0.5):
        self.base_url = base_url.rstrip("/")
        self.delay = delay
        self._client = httpx.Client(
            timeout=30,
            follow_redirects=True,
            headers={"Accept": "application/json"},
        )

    def _get(self, path: str, params: dict | list | None = None) -> dict:
        url = f"{self.base_url}{path}"
        time.sleep(self.delay)
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_categories(self) -> list[CategoryData]:
        data = self._get("/categories.json")
        categories = []
        for cat in data["category_list"]["categories"]:
            categories.append(CategoryData(
                id=cat["id"],
                name=cat["name"],
                slug=cat["slug"],
                topic_count=cat.get("topic_count", 0),
                description=cat.get("description_text") or "",
            ))
        return categories

    def get_category_topics(self, category_slug: str, page: int = 0) -> tuple[list[dict], bool]:
        """Returns (topic_metas, has_more)."""
        try:
            data = self._get(f"/c/{category_slug}.json", {"page": page})
        except httpx.HTTPStatusError as e:
            logger.warning(f"Category {category_slug} page {page} returned {e.response.status_code}")
            return [], False
        topic_list = data.get("topic_list", {})
        topics = topic_list.get("topics", [])
        has_more = "more_topics_url" in topic_list
        return topics, has_more

    def get_topic_posts(self, topic_id: int) -> tuple[dict, list[PostData]]:
        """Fetch topic metadata and ALL posts, handling >20-post pagination."""
        data = self._get(f"/t/{topic_id}.json")
        post_stream = data.get("post_stream", {})
        stream_ids: list[int] = post_stream.get("stream", [])
        initial_posts: list[dict] = post_stream.get("posts", [])

        loaded_ids = {p["id"] for p in initial_posts}
        all_posts = list(initial_posts)

        remaining = [pid for pid in stream_ids if pid not in loaded_ids]
        for i in range(0, len(remaining), CHUNK_SIZE):
            chunk = remaining[i : i + CHUNK_SIZE]
            extra = self._fetch_extra_posts(topic_id, chunk)
            all_posts.extend(extra)

        all_posts.sort(key=lambda p: p["post_number"])
        return data, [self._parse_post(p) for p in all_posts]

    def _fetch_extra_posts(self, topic_id: int, post_ids: list[int]) -> list[dict]:
        time.sleep(self.delay)
        url = f"{self.base_url}/t/{topic_id}/posts.json"
        params = [("post_ids[]", pid) for pid in post_ids]
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response.json().get("post_stream", {}).get("posts", [])

    @staticmethod
    def _parse_post(p: dict) -> PostData:
        return PostData(
            id=p["id"],
            post_number=p["post_number"],
            username=p.get("username", "unknown"),
            created_at=p["created_at"],
            cooked=p.get("cooked", ""),
            reply_to_post_number=p.get("reply_to_post_number"),
            like_count=p.get("like_count", 0),
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "DiscourseClient":
        return self

    def __exit__(self, *args) -> None:
        self.close()
