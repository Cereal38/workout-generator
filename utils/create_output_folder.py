"""Functions that create the final output folder."""

import json
from pathlib import Path


def create_output_folder(json_obj: dict, output_path: str) -> None:
    """Create the final output folder.

    Args:
      json_obj (dict): The JSON object to be saved.
      output_path (str): The path to the output folder.
    """
    # Create the output folder if it does not exist
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Save the JSON object to a file
    with Path(output_path).joinpath("workout.json").open("w") as file:
        json.dump(json_obj, file, indent=4)

    # Get images from the assets folder and copy them to the output folder
    library = json.loads(Path("exercises.json").read_text())
    for exercise in json_obj["exercises"]:
        if exercise["type"] == "exercise":
            for image in library[exercise["id"]]["images"]:
                image_name: str = exercise["name"] + Path(image).name
                Path(output_path).joinpath(image_name).write_bytes(
                    Path("assets/exercises").joinpath(image).read_bytes(),
                )
