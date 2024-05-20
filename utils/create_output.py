"""Functions that create the final output folder."""

import json
from pathlib import Path


def create_output(json_obj: dict, output_path: str) -> None:
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

    # Generate the Markdown file
    generate_markdown(json_obj, output_path)


def generate_markdown(json_obj: dict, output_path: str) -> None:
    """Generate a Markdown file from the given JSON object.

    Args:
      json_obj (dict): The JSON object to be converted.
      output_path (str): The path to the output folder.
    """
    # Create the Markdown file
    with Path(output_path).joinpath("workout.md").open("w") as file:
        file.write("# " + json_obj["name"] + "\n\n")

        file.write("## Infos\n")
        file.write("- **Duration**: " + str(json_obj["duration"]) + "seconds\n")
        file.write("- **Difficulty**: " + str(json_obj["difficulty"]) + "\n")
        file.write("- **Number of sets**: " + str(json_obj["sets"]) + "\n")
        file.write("- **Rest between sets**: " + str(json_obj["rest"]) + "seconds\n")

        file.write("\n## Exercises\n")
        for exercise in json_obj["exercises"]:
            if exercise["type"] == "exercise":
                file.write("### " + exercise["name"] + "\n")
                if exercise["metric"] == "reps":
                    file.write("- **Reps**: " + str(exercise["reps"]) + "\n")
                elif exercise["metric"] == "duration":
                    file.write(
                        "- **Duration**: " + str(exercise["duration"]) + "seconds\n",
                    )
                elif exercise["metric"] == "distance":
                    file.write(
                        "- **Distance**: " + str(exercise["distance"]) + "meters\n",
                    )
                file.write("\n")
            elif exercise["type"] == "rest":
                file.write("### " + exercise["name"] + "\n")
                file.write("- **Duration**: " + str(exercise["duration"]) + "seconds\n")
                file.write("\n")
