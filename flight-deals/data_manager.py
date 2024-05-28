import requests  

#-------------------------------- CONSTANTS --------------------------------#
SHEETY_PRICES_ENDPOINT =  """#Your sheet api prices  # Endpoint for accessing price data"""
BEARER =  """#Your authentication key  # API authentication key"""
SHEET_USERS_ENDPOINT =  """#Your sheet api user data  # Endpoint for accessing user data"""

# DataManager class handles fetching and updating data from Sheety
class DataManager:

    def _init_(self):
        self.destination_data = {}  

    # Method to fetch destination data from Sheety
    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {BEARER}"  # Authorization header with Bearer token
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)  
        data = response.json()  
        self.destination_data = data["prices"]  # Store destination data in instance variable
        return self.destination_data  

    # Method to update destination codes in Sheety
    def update_destination_codes(self):
        for city in self.destination_data:  # Iterate over each city in destination data
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]  
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",  # Construct endpoint for updating specific city
                json=new_data  # Send updated data in JSON format
            )
            print(response.text)  # Print response from Sheety after updating

    # Method to fetch customer emails from Sheety
    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT  # Endpoint for customer data
        headers = {
            "Authorization": f"Bearer {BEARER}"  # Authorization header with Bearer token
        }
        response = requests.get(url=customers_endpoint, headers=headers)  
        data = response.json()  
        self.customer_data = data["users"]  # Store customer data in instance variable
        return self.customer_data
