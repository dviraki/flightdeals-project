class FlightData:
    def _init_(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date, stop_overs=0, via_city=""):
        """
        Initializes an instance of FlightData with the provided parameters.

        Parameters:
            price (float): The price of the flight.
            origin_city (str): The origin city of the flight.
            origin_airport (str): The origin airport code of the flight.
            destination_city (str): The destination city of the flight.
            destination_airport (str): The destination airport code of the flight.
            out_date (str): The departure date of the flight.
            return_date (str): The return date of the flight.
            stop_overs (int): The number of stopovers in the flight route (default is 0).
            via_city (str): The city where the flight has stopovers (default is an empty string).
        """
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

        self.stop_overs = stop_overs
        self.via_city = via_city
