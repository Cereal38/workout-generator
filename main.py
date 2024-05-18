"""Create a workout."""

import argparse

from utils.ai_generation import generate_workout
from utils.create_json import create_json
from utils.create_output_folder import create_output_folder

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", help="The sentence for workout generation")
    parser.add_argument(
        "--no-equipment",
        action="store_true",
        help="Generate a workout without equipment",
    )
    args = parser.parse_args()

    sentence = args.sentence
    no_equipment: bool = args.no_equipment

    answer: str = generate_workout(sentence, no_equipment)
    print("ANSWER:", answer)
    print("")
    json_obj: dict = create_json(answer)
    print("JSON OBJ:", json_obj)
    print("")
    create_output_folder(json_obj, "workout")
