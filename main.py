#!/usr/bin/env python3
import json
import sys


from .config import ProductionConfig, DevelopmentConfig, TestingConfig
from .src import create_app

def config_app(env=None):
    if env is None:
        try:
            env = sys.argv[1]
        except IndexError:
            env = "dev"

    app = create_app()

    match env:
        case "prod":
            app.config.from_object(ProductionConfig)
            with open("/etc/config.json", "r") as f:
                config = json.loads(f.read())
                app.config.from_object(config)
        case "dev":
            app.config.from_object(DevelopmentConfig)  # Disables debug-level logging
        case "debug":
            app.config.from_object(TestingConfig)  # Enables debug-level logging
        case _:
            raise Exception(f"Invalid config!")

    return app

if __name__ == "__main__":
    app = config_app()
    app.run()
