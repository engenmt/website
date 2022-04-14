import flask

flask.cli.load_dotenv()


class Config(object):
    pass


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    SECRET_KEY = "dev"


class TestingConfig(DevelopmentConfig):
    DEBUG = True
