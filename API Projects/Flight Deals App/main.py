# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from pprint import pprint

# class objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# variables
DEPARTURE_CITY_IATA_CODE = "ACC"
data = data_manager.get_data()
sheet_data = data_manager.get_data()
user_data = data_manager.get_user_data()
prices_data = sheet_data['prices']
updated_sheet_data = []

for row in prices_data:
    if row['iataCode'] != "" and row['iataCode'] == flight_search.get_iata_code(row['city']):
        updated_sheet_data.append(row)
    else:
        row['iataCode'] = flight_search.get_iata_code(row['city'])
        updated_sheet_data.append(row)
        data_manager.update_data(row)

date_from = datetime.now().strftime("%d/%m/%Y")
date_to = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")


for destination in updated_sheet_data:
    flight = flight_search.check_flights(
        fly_from=DEPARTURE_CITY_IATA_CODE,
        fly_to=destination['iataCode'],
        date_from=date_from,
        date_to=date_to)

    if flight is not None and flight.price < destination["lowestPrice"]:
        google_flights_link = f"https://www.google.com/flights?hl=en#flt={flight.departure_airport_code}.{flight.destination_airport_code}.{flight.departure_date}*{flight.destination_airport_code}.{flight.departure_airport_code}.{flight.arrival_date} "
        message = f"Low price alert! Only ${flight.price} to fly from" \
                  f"{flight.departure_city}-{flight.departure_airport_code} to " \
                  f"{flight.destination_city}-{flight.destination_airport_code}, " \
                  f"from {flight.departure_date} to {flight.arrival_date}"

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stopovers, via {flight.via_city}"

        # notification_manager.send_message(message_body=message)

        for user in user_data:
            notification_manager.send_email(email=user['email'], message=message, google_flights_link=google_flights_link)
