import requests  

#-------------------------------- CONSTANTS --------------------------------#
BEARER = """#Your authentication key  # API authentication key"""
SHEETY_ENDPOINT = """#Your sheet api users  # Endpoint to post data to Google Sheets"""

def post_new_row(first_name, last_name, email):
    """
    Function to add a new row of data (user information) to Google Sheets.

    Parameters:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.

    Returns:
        None
    """
    # Setting up the headers for the HTTP request
    headers = {
        "Authorization": f"Bearer {BEARER}",  # Including the bearer token for authentication
        "Content-Type": "application/json",  
    }

    # Constructing the body of the request
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    # Making the POST request to add a new row to Google Sheets
    response = requests.post(url=SHEETY_ENDPOINT, headers=headers, json=body)
    response.raise_for_status()  # Raising an error if the request was not successful
    print(response.text)  # Printing the response text (optional)
