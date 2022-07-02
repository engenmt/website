import json
import flask

flask.cli.load_dotenv()


def config():
    with open("/etc/config.json") as config_file:
        config = json.load(config_file)
    return config


class Config(object):
    pass


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    SECRET_KEY = "dev"


class TestingConfig(DevelopmentConfig):
    DEBUG = True
