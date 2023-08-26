import requests

#-------------------------------- CONSTANTS --------------------------------#
BEARER = #Your authentication key
SHEETY_ENDPOINT = #Your sheet api users

def post_new_row(first_name, last_name, email):

    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)