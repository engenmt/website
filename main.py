#!/usr/bin/env python3

from config import DevelopmentConfig, TestingConfig
from src import create_app


if __name__ == "__main__":

    app = create_app()

    # testing = True
    testing = False

    if testing:
        app.config.from_object(TestingConfig)  # Enables debug-level logging
    else:
        app.config.from_object(DevelopmentConfig)  # Disables debug-level logging

    app.run(host="localhost", port=5000)
