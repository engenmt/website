#!/usr/bin/env python3
import json
import sys


from config import DevelopmentConfig, TestingConfig
from src import create_app


if __name__ == "__main__":

    app = create_app()

    try:
        env = sys.argv[1]
    except IndexError:
        env = "dev"

    match env:
        case "prod":
            with open("/etc/config.json", "r") as f:
                config = json.loads(f.read())
                app.config.from_object(config)
        case "dev":
            app.config.from_object(DevelopmentConfig)  # Disables debug-level logging
        case "debug":
            app.config.from_object(TestingConfig)  # Enables debug-level logging
        case _:
            raise Exception(f"Invalid config!")
        
    app.run(host="localhost", port=5000)
