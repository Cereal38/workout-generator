"""Contains functions that allow to create a JSON file from a string."""

from pathlib import Path


def json_create(output_path: str, content: str) -> None:
    """Creates a JSON file from a string.

    Args:
        output_path (str): The path to the output JSON file.
        content (str): The content of the JSON file.
    """
    with Path(output_path).open("w") as f:
        f.write(content)
