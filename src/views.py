from flask import render_template, Blueprint

bp = Blueprint("views", __name__)


@bp.route("/")
def home() -> str:
    return render_template("hello.html")
