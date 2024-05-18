"""Functions that create the final output folder."""

import json
from pathlib import Path


def create_output_folder(json_obj: dict, output_path: str) -> None:
    """Create the final output folder.

    Args:
      json_obj (dict): The JSON object to be saved.
      output_path (str): The path to the output folder.
    """
    # Remove the output folder if it already exists
    if Path(output_path).exists():
        for file in Path(output_path).iterdir():
            file.unlink()
        Path(output_path).rmdir()

    # Create the output folder
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Save the JSON object to a file
    with Path(output_path).joinpath("workout.json").open("w") as file:
        json.dump(json_obj, file, indent=4)

    # Get images from the assets folder and copy them to the output folder
    library = json.loads(Path("exercises.json").read_text())
    for exercise in json_obj["exercises"]:
        if exercise["type"] == "exercise":
            for image in library[exercise["id"]]["images"]:
                Path(output_path).joinpath(image).write_bytes(
                    Path("assets").joinpath(image).read_bytes(),
                )
