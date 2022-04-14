from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import views

    app.register_blueprint(views.bp)
    app.add_url_rule("/", endpoint="views.home")

    return app
