import requests
import datetime as dt


# functions
def post_request(api_endpoint, json_data, auth_headers):
    response = requests.post(url=api_endpoint, json=json_data, headers=auth_headers)
    response.raise_for_status()
    return response.json()


# constants
NUTRITIONIX_APP_ID = "21659f24"
NUTRITIONIX_APP_KEY = "d34b4959ae0acba1ed4d112790298713"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/2b19ebd89a834491a7f81a5bf5f84b61/workoutTracking/workouts"

# headers
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}

auth_header = {
    "Authorization": "Bearer jefftheasante"
}

# variables
gender = "male"
weight = 84
height = 184
age = 23
query = input("What did you do today?: ")
date = dt.datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
formatted_time = date.strftime("%X")


data = {
    "query": query,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

post_data = post_request(api_endpoint=f"{NUTRITIONIX_ENDPOINT}natural/exercise", json_data=data, auth_headers=headers)

# for each exercise, get the following values
for exercise in post_data['exercises']:
    # sheety requires data to be nested in a dictionary
    sheety_input = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

sheety_post = post_request(api_endpoint=SHEETY_POST_ENDPOINT, json_data=sheety_input, auth_headers=auth_header)
print(sheety_post)







