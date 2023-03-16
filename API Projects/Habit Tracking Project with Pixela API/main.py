import requests
import datetime as dt

current_date = dt.datetime.now()
date_formatted = current_date.strftime("%Y%m%d")
print(date_formatted)


def post_requests(endpoint, params, headers):
    response = requests.post(url=endpoint, json=params, headers=headers)

    return response.json()

def put_requests(endpoint, params, headers):
    response = requests.put(url=endpoint, json=params, headers=headers)

    return response.json()

def delete_requests(endpoint, headers):
    response = requests.delete(url=endpoint, headers=headers)

    return response


    return response.json()


USERNAME = "jeffkobby"
GRAPH_ID = "graph1"
TOKEN = "q7#*s5K?Q1vD#Dv5"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "kuro"
}

post_pixel_params = {
    "date": date_formatted,
    "quantity": "20",
}

update_pixel_params = {
    "quantity": "16"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

post_pixel = post_requests(endpoint=POST_PIXEL_ENDPOINT, params=post_pixel_params, headers=headers)
update_pixel = put_requests(endpoint=UPDATE_PIXEL_ENDPOINT, params=update_pixel_params, headers=headers)
delete_pixel = delete_requests(endpoint=UPDATE_PIXEL_ENDPOINT, headers=headers)




