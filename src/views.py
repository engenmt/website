from flask import render_template, Blueprint

from .articles import get_articles
from .software import get_software

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


@bp.route("/permpy")
def permpy_view() -> str:
    wheel_name = "wheels/permpy-0.2.1-py3-none-any.whl"
    return render_template("permpy-repl.html", wheel_name=wheel_name)


@bp.route("/enumerate")
def permpy_enumerate() -> str:
    wheel_name = "wheels/permpy-0.2.1-py3-none-any.whl"
    return render_template("permpy-enumerate.html", wheel_name=wheel_name)
