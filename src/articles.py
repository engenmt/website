from flask import current_app
from .utils import choose_image, create_authors_string
import yaml


def create_links(article: dict) -> list[tuple[str, str]]:
    links: list[tuple[str, str]] = []
    if "arxiv" in article:
        links.append(("arXiv", article["arxiv"]))
    if "journal" in article:
        journal = article["journal"]
        links.append((journal["title"], journal["link"]))

    return links


def choose_image(article: dict) -> str:
    images: dict = article["images"]
    image: str = images.get("small", images.get("medium", images.get("large")))
    return f"content/{image}"


def get_articles() -> list[dict]:
    with current_app.open_resource("articles.yaml") as f:
        my_articles: list[dict] = yaml.load(f, Loader=yaml.Loader)

    for article in my_articles:
        article["authors"] = create_authors_string(article["authors"])
        article["links"] = create_links(article)
        article["image"] = choose_image(article)

    return my_articles
