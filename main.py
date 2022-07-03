#!/usr/bin/env python3
import json
import sys


def create_app_prod():
    from config import ProductionConfig
    from src import create_app

    app = create_app()

    app.config.from_object(ProductionConfig)
    with open("/etc/config.json", "r") as f:
        config = json.loads(f.read())
        app.config.from_object(config)
    
    return app


def create_app_dev(env=None):
    from .config import DevelopmentConfig, TestingConfig
    from .src import create_app

    app = create_app()

    match env:
        case "dev":
            app.config.from_object(DevelopmentConfig)  # Disables debug-level logging
        case "debug":
            app.config.from_object(TestingConfig)  # Enables debug-level logging
        case _:
            raise Exception(f"Invalid config!")
    
    return app






if __name__ == "__main__":
    try:
        env = sys.argv[1]
    except IndexError:
        env = "dev"

    app = create_app_dev(env)
    app.run()
