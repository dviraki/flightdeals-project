Flight Deals Project

This project aims to find the best flight deals and notify users via email. It utilizes APIs to search for flight information, store user data, and send email alerts for price drops.
Setup

    Install Python (if not already installed).
    Install required dependencies using pip install -r requirements.txt.
    Update the following constants in the code:
        BEARER: Your authentication key for accessing the Sheety API.
        SHEETY_ENDPOINT: The endpoint for the Sheety API users.
        SHEETY_PRICES_ENDPOINT: The endpoint for the Sheety API prices.
        SHEET_USERS_ENDPOINT: The endpoint for the Sheety API user data.
        TEQUILA_ENDPOINT: The endpoint for the Tequila API.
        TEQUILA_API_KEY: Your API key for the Tequila API.
        ORIGIN_CITY_IATA: The IATA code for the origin city airport.
        MY_EMAIL: Your email address for sending notifications.
        PASSWORD: Your email app password.
        EMAIL_PROVIDER: Your email provider (e.g., Gmail, Yahoo, etc.).

Usage

    Run the main.py file to start the application.
    Follow the prompts to input your first name, last name, and email address.
    The application will search for flight deals and send email alerts for price drops.
    You can quit the application at any time by typing "quit" or "exit".
