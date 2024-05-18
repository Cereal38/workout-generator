# main.py

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = sys.argv[1]
        print(f"You entered the sentence: {sentence}")
    else:
        print("Please provide a sentence as an argument.")
