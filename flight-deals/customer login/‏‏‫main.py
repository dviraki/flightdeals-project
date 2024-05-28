import sheety  

# Introduction message
print("Welcome to flight-101 club \n \
We find the best flight deals and email them to you.")

# Asking for user's first name and last name
first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

# Initializing email and email verification variables
email = "email1"
email_verification = "email2"

# Loop until email and its verification match or user opts to quit
while email != email_verification:
    email = input("What is your email? ")
    if email.lower() == "quit" or email.lower() == "exit":  # Allowing the user to quit
        exit()
    email_verification = input("Please verify your email : ")
    if email_verification.lower() == "quit" or email_verification.lower() == "exit":  # Allowing the user to quit
        exit()

# Confirmation message upon successful registration
print("OK. You're in the club!")

# Call the function to add user information to the database
sheety.post_new_row(first_name, last_name, email)
