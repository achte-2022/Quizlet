# IMPORTING LIBRARIES
import requests

# CONSTANTS
QUIZ_API_ENDPOINT = "https://opentdb.com/api.php"
NUM_QUESTIONS = 10
QUIZ_TYPE = "boolean"
DATA_FILE = "data.py"

quiz_parameters = {"amount": NUM_QUESTIONS, "type": QUIZ_TYPE}

quiz_response = requests.get(url=QUIZ_API_ENDPOINT, params=quiz_parameters)
quiz_response.raise_for_status()
question_data = quiz_response.json()["results"]
