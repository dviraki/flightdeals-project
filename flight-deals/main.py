from datetime import datetime, timedelta
from data_manager import DataManager 
from flight_search import FlightSearch  
from notification_manager import NotificationManager  

#-------------------------------- CONSTANTS --------------------------------#
ORIGIN_CITY_IATA = """#origin airport  # Define constant for the origin airport IATA code"""

#-------------------------------- CLASS VARIABLES --------------------------------#
data_manager = DataManager()  
notification_manager = NotificationManager()  
flight_search = FlightSearch()  

# Getting destination data from the data manager
sheet_data = data_manager.get_destination_data()  

# Update the destination codes if not already done
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)  # Get destination codes
    data_manager.update_destination_codes()  # Updating destination codes in the data manager
    sheet_data = data_manager.get_destination_data()  # Getting updated destination data

# Creating a dictionary of destinations with their details
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# Define time range for flight search
tomorrow = datetime.now() + timedelta(days=1)  
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))  

# Check for cheap flights
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # Send email to alert for lower price
    if (flight is not None) and (flight.price < destination["lowestPrice"]):
        users = data_manager.get_customer_emails()  # Getting customer emails from the data manager
        emails = [row["email"] for row in users]  
        names = [row["firstName"] for row in users]  

        # Construct notification message
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, message)  # Sending notification emails to users





