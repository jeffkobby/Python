import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

api_key = "c155d787bd874e0e4c2545544856c3c9"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

# twilio account credentials
twilio_sid = "AC3710e934e179ccba277bc5f83daa1d94"
twilio_auth_token = "2f5334670a6a6a19d643ee55a6503cac"


parameters = {
    "lat": "-15.387526",
    "lon": "28.322817",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

# connect to OpenWeather API
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# get weather data for the next 12 hours
sliced_hourly_data = weather_data['hourly'][0:12]


will_rain = False

# value of 'weather' is a list of dictionaries
for hour_data in sliced_hourly_data:
    weather_id = hour_data['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_sid, twilio_auth_token, http_client=proxy_client)
    client.messages.create(to="=+233505043400", from_="+17755228278", body="Bring an umbrella☔")

