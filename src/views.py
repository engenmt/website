from flask import render_template, Blueprint
from src.articles import get_articles
from src.software import get_software

bp = Blueprint("views", __name__)


@bp.route("/")
@bp.route("/home")
def home() -> str:
    return render_template("base.html")


@bp.route("/research")
def research() -> str:
    my_articles = get_articles()
    return render_template("articles.html", my_articles=my_articles)


@bp.route("/software")
def software() -> str:
    my_software = get_software()
    return render_template("software.html", my_software=my_software)


@bp.route("/about")
def about() -> str:
    return render_template("base.html")


@bp.route("/articles")
def articles() -> str:
    return render_template("base.html")
