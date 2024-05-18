"""Create a workout."""

import sys

from utils.json_extract import json_extract

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = sys.argv[1]
    else:
        sys.exit("Please provide a sentence as an argument.")

    # Extract the exercises from the JSON file
    exercises: list[dict[str, str]] = json_extract("exercises_simple.json")
