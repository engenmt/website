from flask import current_app
from .utils import choose_image, create_authors_string
import yaml


def get_software() -> list[dict]:
    with current_app.open_resource("software.yaml") as f:
        my_software: list[dict] = yaml.load(f, Loader=yaml.Loader)

    for software in my_software:
        software["authors"] = create_authors_string(software["authors"])
        software["image"] = choose_image(software["images"])

    return my_software
