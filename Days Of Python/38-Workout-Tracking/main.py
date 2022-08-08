import requests
from datetime import datetime
import os

############### GLOBAL VARIABLES ###############

GENDER = "Male"
WEIGHT_KG = 73.9
HEIGHT_CM = 175.3
AGE = 21

APP_ID = os.environ["bb7f6e1d"]
API_KEY = os.environ["98238a3ac7dc9441480e4d0b7aab4597"]


############### ENDPOINT SETUPS ###############

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a42fa8b3975fee3420f30a5d825612f4/[100DaysOfPython]MyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


############### SHEETY INPUTS ###############

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
