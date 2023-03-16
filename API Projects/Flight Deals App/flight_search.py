import requests
from flight_data import FlightData
from pprint import pprint

API_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "cw7J6fHVkuESuIo-OTeIMJWtUYQgBB3N"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city):
        """"Get the IATA code of the city passed into the function"""
        location_endpoint = f"{API_ENDPOINT}/locations/query"
        header = {"apikey": API_KEY}
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{location_endpoint}", params=query, headers=header)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]

        return code

    def check_flights(self, fly_from, fly_to, date_from, date_to):
        """"Function to check for available flights within a period"""
        header = {
            "apikey": API_KEY
        }

        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "one_for_city": 1,
            "curr": "USD",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round"
        }

        response = requests.get(url=f"{API_ENDPOINT}/v2/search", params=params, headers=header)
        response.raise_for_status()
        result = response.json()

        try:
            # Get flight data
            data = result["data"][0]
        except IndexError:
            for stopover in range(1,4):
                params['max_stopovers'] = stopover
                response = requests.get(url=f"{API_ENDPOINT}/v2/search", params=params, headers=header)
                response.raise_for_status()
                result = response.json()

                if stopover == 1:
                    if len(result["data"]) != 0:
                        data = result["data"][0]
                        route = data['route']
                        flight_data = FlightData(
                            departure_city=route[0]['cityFrom'],
                            departure_airport_code=route[0]['flyFrom'],
                            destination_city=route[1]['cityTo'],
                            destination_airport_code=route[1]['flyTo'],
                            price=data['price'],
                            departure_date=route[0]['local_departure'].split('T')[0],
                            arrival_date=route[2]['local_departure'].split('T')[0],
                            stop_overs=1,
                            via_city=f"{route[0]['cityTo']}"
                        )
                        return flight_data
                        break
                    else:
                        continue

                if stopover == 2:
                    if len(result["data"]) != 0:
                        data = result["data"][0]
                        route = data['route']
                        flight_data = FlightData(
                            departure_city=route[0]['cityFrom'],
                            departure_airport_code=route[0]['flyFrom'],
                            destination_city=route[1]['cityTo'],
                            destination_airport_code=route[1]['flyTo'],
                            price=data['price'],
                            departure_date=route[0]['local_departure'].split('T')[0],
                            arrival_date=route[3]['local_departure'].split('T')[0],
                            stop_overs=2,
                            via_city=f"{route[0]['cityTo']} and finally {route[1]['cityTo']}"
                        )
                        return flight_data
                        break
                    else:
                        continue

                if stopover == 3:
                    if len(result["data"]) != 0:
                        data = result["data"][0]
                        route = data['route']
                        flight_data = FlightData(
                            departure_city=route[0]['cityFrom'],
                            departure_airport_code=route[0]['flyFrom'],
                            destination_city=route[2]['cityTo'],
                            destination_airport_code=route[2]['flyTo'],
                            price=data['price'],
                            departure_date=route[0]['local_departure'].split('T')[0],
                            arrival_date=route[3]['local_departure'].split('T')[0],
                            stop_overs=3,
                            via_city=f"{route[0]['cityTo']}, {route[1]['cityTo']} and finally {route[2]['cityTo']}"
                        )
                        return flight_data
                        break
                    else:
                        print(f"No availabe flights to {fly_to}")
                        return None

        else:
            # pass flight data values from API into FlightData class
            flight_data = FlightData(
                departure_city=data["cityFrom"],
                departure_airport_code=data["cityCodeFrom"],
                destination_city=data["cityTo"],
                destination_airport_code=data["cityCodeTo"],
                price=data['price'],
                departure_date=data['route'][0]['local_departure'].split("T")[0],
                arrival_date=data['route'][1]['local_departure'].split("T")[0]
            )
            return flight_data
