import requests
from datetime import datetime

MY_LAT = 5.634150
MY_LONG = -0.171150
API_ENDPOINT = "https://api.sunrise-sunset.org/json"
time_now = datetime.now()

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}


response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

sunrise_time = data['results']['sunrise']
sunset_time = data['results']['sunset']


print(sunrise_time)
print(time_now.time())
