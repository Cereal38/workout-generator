"""Contains functions that allow to create a JSON file from a string."""

import json
from pathlib import Path


def add_images(json_obj: dict) -> dict:
    """Adds the images to the JSON file.

    Args:
        json_obj (dict): The JSON object to which the images should be added.

    Returns:
        dict: The JSON object with the images added.
    """
    # Convert the main library to a Python object
    library = json.loads(Path("exercises.json").read_text())

    # For each exercise, get the images from the original JSON file and add them to the new JSON file
    for exercise in json_obj["exercises"]:
        if exercise["type"] == "exercise":
            exercise["images"] = library[exercise["id"]]["images"]

    # Convert the Python object back to a JSON string and return it
    return json_obj


def create_json(content: str) -> dict:
    """Generate a JSON object from a string and add informations.

    Args:
        output_path (str): The path to the output JSON file.
        content (str): The content of the JSON file as a string.
    """
    # Remove everything before the first '{' character
    # And remove everything after the last '}' character
    content = content[content.find("{") : content.rfind("}") + 1]

    # Convert to a Python object
    json_obj: dict = json.loads(content)

    # Add the images to the JSON object
    json_obj = add_images(json_obj)

    return json_obj
