"""Contains functions that allow to extract information from a JSON file."""

import json
from pathlib import Path


def json_extract(input_file: str) -> list[dict[str, str]]:
    """Extracts the name and equipment of each exercise from a JSON file.

    Args:
      input_file (str): The path to the initial JSON file.

    Returns:
      list[dict[str, str]]: A list of dictionaries containing the name and equipment of each exercise.
    """
    with Path(input_file).open() as f:
        data = json.load(f)

    return [
        {"name": exercise["name"], "equipment": exercise["equipment"]}
        for exercise in data
    ]
