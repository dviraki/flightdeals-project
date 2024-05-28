import requests  
from flight_data import FlightData  

#-------------------------------- CONSTANTS --------------------------------#
TEQUILA_ENDPOINT =  """Your Tequila api  # Endpoint for accessing Tequila API"""
TEQUILA_API_KEY =  """Your api key  # API key required for accessing Tequila API"""

class FlightSearch:

    def _init_(self):
        """
        Initializes an instance of FlightSearch with an empty list for storing city codes.
        """
        self.city_codes = []

    def get_destination_code(self, city_names):
        """
        Retrieves destination codes for the provided city names.

        Parameters:
            city_names (list): A list of city names for which destination codes are to be retrieved.

        Returns:
            list: A list of destination codes corresponding to the provided city names.
        """
        print("get destination codes triggered")
        headers = {"apikey": TEQUILA_API_KEY}
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        for city in city_names:
            query = {"term": city, "location_types": "city"}

            #Api call
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Checks for available flights between origin and destination cities within specified time range.

        Parameters:
            origin_city_code (str): The origin city code.
            destination_city_code (str): The destination city code.
            from_time (datetime): The starting date for flight departure.
            to_time (datetime): The ending date for flight departure.

        Returns:
            FlightData or None: FlightData object containing flight details if available, otherwise None.
        """
        print(f"Check flights triggered for {destination_city_code}")
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        #no stop flight
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            # one stop flight
            try:
                data = response.json()["data"][0]
            except IndexError:
                print("No flight was found")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: ${flight_data.price}")
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
