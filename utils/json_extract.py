"""Contains functions that allow to extract information from a JSON file."""

import json
from pathlib import Path


def json_extract(input_file: str, no_equipment: bool = False) -> list[dict[str, str]]:
    """Extracts the name and if of each exercise from a JSON file.

    Args:
      input_file (str): The path to the initial JSON file.
      no_equipment (bool): Whether the exercises should require equipment.

    Returns:
      list[dict[str, str]]: A list of dictionaries containing the name and equipment of each exercise.
    """
    with Path(input_file).open() as f:
        data = json.load(f)

    # If no_equipment is True, exclude exercises that require equipment
    if no_equipment:
        return [
            {"name": exercise["name"], "id": exercise["id"]}
            for exercise in data
            if exercise["equipment"] is None or exercise["equipment"] == "body only"
        ]

    return [
        {
            "name": exercise["name"],
            "id": exercise["id"],
        }
        for exercise in data
    ]
