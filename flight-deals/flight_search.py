import requests
from flight_data import FlightData

#-------------------------------- CONSTANTS --------------------------------#
TEQUILA_ENDPOINT =  #Your Tequila api
TEQUILA_API_KEY =  #Your api key

class FlightSearch:

    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_names):

        print("get destination codes triggered")
        #header, api and params
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

    # looking only for direct flights, that leave anytime between tomorrow and in 6 months time.
    # We're also looking for round trips that return between 7 and 28 days in length.
    # The currency of the price we get back is shekels.
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
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

        #one stop flight
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            # no stop flight
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
            return flight_data
