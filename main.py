"""Create a workout."""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = sys.argv[1]
    else:
        sys.exit("Please provide a sentence as an argument.")
