import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/2b19ebd89a834491a7f81a5bf5f84b61/flightDealsTracking/prices"
        self.SHEETY_USERS_ENDPOINT = "https://api.sheety.co/2b19ebd89a834491a7f81a5bf5f84b61/flightDealsTracking/users"


    def get_data(self):
        """"Get values in our Google Sheet with Sheety"""
        response = requests.get(url=self.SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()

        return data

    def update_data(self, row):
        """"Update IATA CODE for new sheet entries"""
        new_data = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(url=f"{self.SHEETY_PRICES_ENDPOINT}/{row['id']}",
                                json=new_data
                                )
        response.raise_for_status()

    def get_user_data(self):
        response = requests.get(url=self.SHEETY_USERS_ENDPOINT)
        response.raise_for_status()
        result = response.json()['users']

        return result

