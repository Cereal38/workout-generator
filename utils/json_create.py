"""Contains functions that allow to create a JSON file from a string."""

from pathlib import Path


def json_create(output_path: str, content: str) -> None:
    """Creates a JSON file from a string.

    Args:
        output_path (str): The path to the output JSON file.
        content (str): The content of the JSON file.
    """
    # Remove everything before the first '{' character
    # And remove everything after the last '}' character
    content = content[content.find("{") : content.rfind("}") + 1]

    with Path(output_path).open("w") as f:
        f.write(content)
