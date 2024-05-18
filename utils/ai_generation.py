"""This module contains the function to generate the workout using AI."""

import os
import sys

from dotenv import load_dotenv

# from openai import OpenAI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from utils.json_extract import json_extract

MODEL = "open-mixtral-8x7b"
# MODEL = "mistral-large-latest"
MAX_TOKENS = 400


def generate_workout(instructions: str) -> str:
    """Generate a workout following the instructions given by the user.

    Args:
        instructions (str): The instructions provided by the user.

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
    exercises: list[dict[str, str]] = json_extract("exercises_simple.json")

    # Generate script
    messages = [
        ChatMessage(
            role="system",
            content="""You are an experimented sport coach.
                    You are doing this job for 10 years.
                    You got a dictionnary containing all the exercises you can use.
                    You are creating a workout for a client.
                    The client is a 25 years old doint sport 3 times a week.
                    The client will give you more informations about his workout in the next message, follow his instructions.
                    You must format your workout as a json file with the following structure:
                    {
                        "name": "Name of the workout",
                        "description": "Description of the workout",
                        "duration": "Estimated duration of the workout",
                        "diffulty": "Difficulty level of the workout (1 to 5)",
                        "exercises": [
                            {
                                "name": "Name of the exercise (Exact name from the dictionnary)",
                                "type": "Type of the exercise (reps, time, distance, ...)",
                                "reps": "Number of repetitions (if type is reps)",
                                "time": "Duration of the exercise (if type is time)",
                                "distance": "Distance to cover (if type is distance)",
                            },
                            ...
                        ]
                    }
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
