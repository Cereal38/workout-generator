"""Create a workout."""

import sys

from utils.ai_generation import generate_workout

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = sys.argv[1]
    else:
        sys.exit("Please provide a sentence as an argument.")

    answer: str = generate_workout(sentence)
    print(answer)
