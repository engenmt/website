from flask import current_app
import yaml


LOREM_IPSUM = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
    "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
    "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
    "in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
    "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
    "sunt in culpa qui officia deserunt mollit anim id est laborum."
)


def create_authors_string(authors):
    if len(authors) >= 2:
        authors[-1] = f"and {authors[-1]}"
    if len(authors) >= 3:
        return ", ".join(authors)

    return " ".join(authors)


def create_links(article):
    links = []
    if "arxiv" in article:
        links.append(("arXiv", article["arxiv"]))
    if "journal" in article:
        journal = article["journal"]
        links.append((journal["title"], journal["link"]))

    return links


def get_articles():
    with current_app.open_resource("static/content/articles.yaml") as f:
        my_articles = yaml.load(f, Loader=yaml.Loader)

    for article in my_articles:
        article["authors_string"] = create_authors_string(article["authors"])
        article["links"] = create_links(article)

        if "abstract" not in article:
            article["abstract"] = LOREM_IPSUM

        article["image"] = f"content/{article.get('image', 'universal-4.png')}"

    return my_articles
