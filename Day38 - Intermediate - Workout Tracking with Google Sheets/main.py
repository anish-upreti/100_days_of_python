import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 169
AGE = 21

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
# APP_ID = os.environ["ENV_NIX_APP_ID"]
# API_KEY = os.environ["ENV_NIX_API_KEY"]
APP_ID = "2931e1ba"
API_KEY = "c84ef5a0a8f32302f1571c7dbdca2b9a"
BEARER_TOKEN = "adjflasd456@#$12uio"

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0ac83938c3b5ceb33bfd9ef3bc57b612/copyOfMyWorkouts/workouts"

question = input("Which exercises did you do?\n")

params = {
    "query": question,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=api_endpoint, json=params, headers=header)
result = response.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

bearer_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, headers=bearer_header)

    print(sheety_response.text)
