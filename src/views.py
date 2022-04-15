from flask import render_template, Blueprint
from src.articles import get_articles

bp = Blueprint("views", __name__)


@bp.route("/")
def home() -> str:
    return render_template("hello.html")


@bp.route("/articles")
def articles() -> str:
    my_articles = get_articles()
    return render_template("articles.html", articles=my_articles)
