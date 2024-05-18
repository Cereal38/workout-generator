"""Contains functions that allow to create a JSON file from a string."""

import json
from pathlib import Path


def add_images(content: str) -> str:
    """Adds the images to the JSON file.

    Args:
        content (str): The content of the JSON file.

    Returns:
        str: The content of the JSON file with the images added.
    """
    # Convert the JSON string to a Python object
    json_obj = json.loads(content)

    # Convert the main library to a Python object
    library = json.loads(Path("exercises.json").read_text())

    # For each exercise, get the images from the original JSON file and add them to the new JSON file
    for exercise in json_obj["exercises"]:
        if exercise["type"] == "exercise":
            exercise["images"] = library[exercise["id"]]["images"]

    # Convert the Python object back to a JSON string and return it
    return json.dumps(json_obj, indent=2)


def create_json(output_path: str, content: str) -> None:
    """Creates a JSON file from a string.

    Args:
        output_path (str): The path to the output JSON file.
        content (str): The content of the JSON file as a string.
    """
    # Remove everything before the first '{' character
    # And remove everything after the last '}' character
    content = content[content.find("{") : content.rfind("}") + 1]

    content = add_images(content)

    with Path(output_path).open("w") as f:
        f.write(content)
