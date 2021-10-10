import os
from datetime import datetime
import requests
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
shetty_url = "https://api.sheety.co/281c459fd63d9fbc2798cb8c4c5d3fda/workoutTracking/workouts"
HEADERS = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_API_KEY")

}
parameters = {
    "query": exercise_text,
    "gender": os.environ.get("GENDER"),
    "weight_kg": os.environ.get("WEIGHT_KG"),
    "height_cm": os.environ.get("HEIGHT_CM"),
    "age": os.environ.get("AGE")
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=HEADERS)
result = response.json()
print(result)
workout_values = result["exercises"][0]


today = datetime.now()
formatted_date = str(today.strftime("%d/%m/%Y"))
formatted_time = str(today.strftime("%X"))
header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer asdf123.lkjh,/"
}

for exercise in result["exercises"]:
    body = {
      "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "duration": workout_values["duration_min"],
            "calories": workout_values["nf_calories"],
            "exercise": workout_values["name"].title()
      }
    }
    sheety_response = requests.post(url=shetty_url, json=body, headers=header)
    print(sheety_response.text)
# shetty_data =
# print(shetty_data)

# var = {'exercises':
#     [{
#         'tag_id': 317,
#         'user_input': 'ran',
#         'duration_min': 30.02,
#         'met': 9.8,
#         'nf_calories': 392.26,
#         'photo':
#             {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
#              'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
#              'is_user_uploaded': False
#              },
#         'compendium_code': 12050,
#         'name': 'running',
#         'description': None,
#         'benefits': None}]}

