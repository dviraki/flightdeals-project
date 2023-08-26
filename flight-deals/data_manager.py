import requests

#-------------------------------- CONSTANTS --------------------------------#
SHEETY_PRICES_ENDPOINT =  #Your sheet api prices
BEARER =  #Your authentication key
SHEET_USERS_ENDPOINT =  #Your sheet api user data

#main job is to get and update data from sheety as out data base
class DataManager:

    def __init__(self):
        self.destination_data = {}

    #GET data from Sheety
    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {BEARER}"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    #Updating the Google sheet in Sheety
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        headers = {
            "Authorization": f"Bearer {BEARER}"
        }
        response = requests.get(url=customers_endpoint,headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data