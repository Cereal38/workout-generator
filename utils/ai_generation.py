"""This module contains the function to generate the workout using AI."""

import os
import sys

from dotenv import load_dotenv

# from openai import OpenAI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from utils.get_exercises import get_exercices

# MODEL = "open-mistral-7b"
MODEL = "open-mixtral-8x7b"
# MODEL = "mistral-large-latest"
MAX_TOKENS = 500
INPUT_FILE = "exercises.json"


def generate_workout(instructions: str, no_equipment: bool = False) -> str:
    """Generate a workout following the instructions given by the user.

    Args:
        instructions (str): The instructions provided by the user.
        no_equipment (bool): Whether the exercises should require equipment.

    Returns:
        str: The generated workout.
    """
    # Setup API key
    load_dotenv()
    api_key = os.getenv("MISTRAL_API_KEY")
    if api_key is None:
        sys.exit("Please provide the API key in the .env file.")

    client = MistralClient(api_key=api_key)

    # Extract the exercises from the JSON file
    exercises: list[dict[str, str]] = get_exercices(INPUT_FILE, no_equipment)

    # Generate script
    messages = [
        ChatMessage(
            role="system",
            content="""You are an experimented sport coach.
                    You are doing this job for 10 years.
                    You are creating a workout for a client.
                    The client is a 25 years old doint sport 3 durations a week.
                    The client will give you more informations about his workout in the next message, follow his instructions.
                    You got a dictionnary containing all the exercises you can use. You're only allowed to use the exercises from this dictionnary.
                    You can also add rest between exercises.
                    A set must end with an exercise.
                    Because rest aren't in the dictionnaty, do not add an ID and imagine the rests name.
                    You must format your workout as a json file with the following structure:
                    {
                        "name": "Name of the workout",
                        "duration": "Estimated duration of the workout (int in seconds)",
                        "difficulty": "Difficulty level of the workout (int from 1 to 5)",
                        "sets": "Number of sets (int)",
                        "rest": "Rest duration between sets (int in seconds)",
                        "exercises": [
                            {
                                "name": "Name of the exercise (Exact name from the dictionnary)",
                                "type": "Type of the exercise (exercise, rest)",
                                "metric": "Metric of the exercise (reps, duration, distance)",
                                "reps": "Number of repetitions (int - only if metric is reps)",
                                "duration": "Duration of the exercise (int in seconds - only if metric is duration or is it is a rest)",
                                "distance": "Distance to cover (int in meters - only if metric is distance)",
                                "id": "Id of the exercise (Exact id from the dictionnary)"
                            },
                            ...
                        ]
                    }
                    Here is an example of a workout (to show the structure):
                    {
                        "name": "Full body workout",
                        "duration": 3600,
                        "difficulty": 3,
                        "sets": 3,
                        "rest": "Rest duration between sets (int in seconds)",
                        "exercises": [
                            {
                                "name": "Pushups",
                                "type": "exercise",
                                "metric": "reps",
                                "reps": 15,
                                "id": 567
                            },
                            {
                                "name": "Rest",
                                "type": "rest",
                                "duration": 60
                            },
                            {
                                "name": "Plank",
                                "type": "exercise",
                                "metric": "duration",
                                "duration": 60,
                                "id": 538
                            }
                        ]
                    }
                    Your answer must contains only the workout, nothing else.
                    Here is the dictionnary of exercises you can use:
                    """
            + str(exercises),
        ),
    ]

    messages.append(ChatMessage(role="user", content=instructions))

    response = client.chat(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=messages,
    )

    return response.choices[0].message.content
