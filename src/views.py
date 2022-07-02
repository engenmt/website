from flask import render_template, Blueprint
from .articles import get_articles

bp = Blueprint("views", __name__)


@bp.route("/")
@bp.route("/home")
def home() -> str:
    return render_template("base.html")


@bp.route("/research")
def research() -> str:
    my_articles = get_articles()
    return render_template("articles.html", articles=my_articles)


@bp.route("/software")
def software() -> str:
    return render_template("base.html")


@bp.route("/about")
def about() -> str:
    return render_template("base.html")


@bp.route("/articles")
def articles() -> str:
    return render_template("base.html")
