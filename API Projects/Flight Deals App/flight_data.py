class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, departure_city, departure_airport_code, destination_city, destination_airport_code, price,
                 departure_date, arrival_date, stop_overs=0, via_city=""):
        self.departure_city = departure_city
        self.departure_airport_code = departure_airport_code
        self.destination_city = destination_city
        self.destination_airport_code = destination_airport_code
        self.price = price
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.stop_overs = stop_overs
        self.via_city = via_city






