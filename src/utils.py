def create_authors_string(authors: list[str]) -> str:
    if len(authors) >= 2:
        authors[-1] = f"and {authors[-1]}"
    if len(authors) >= 3:
        return ", ".join(authors)

    return " ".join(authors)


def choose_image(images) -> str:
    image: str = images.get("small", images.get("medium", images.get("large")))
    return f"content/{image}"
