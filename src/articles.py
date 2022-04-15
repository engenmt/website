from flask import current_app
import yaml


def create_authors_string(authors):
    if len(authors) >= 2:
        authors[-1] = f"and {authors[-1]}"
    if len(authors) >= 3:
        return ", ".join(authors)

    return " ".join(authors)


def get_articles():
    with current_app.open_resource("static/content/articles.yaml") as f:
        my_articles = yaml.load(f, Loader=yaml.Loader)

    for article in my_articles:
        article["authors_string"] = create_authors_string(article["authors"])
    return my_articles
