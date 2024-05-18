"""Contains functions that reduce the size of the initial JSON file."""

import json
from pathlib import Path


def reduce_json(input_file: str, output_file: str) -> None:
    """Reduce the size of a JSON file by only keeping the 'name' and 'equipment' fields."""
    with Path(input_file).open() as f:
        data = json.load(f)

    new_data = [
        {"name": exercise["name"], "equipment": exercise["equipment"]}
        for exercise in data
    ]

    with Path(output_file).open("w") as f:
        json.dump(new_data, f, indent=1)
