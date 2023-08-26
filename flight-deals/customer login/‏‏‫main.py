import sheety

print("Welcome to flight-101 club \n \
We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email = "email1"
email_verifecation = "email2"

while email != email_verifecation:
  email = input("What is your email? ")
  if email.lower() == "quit" \
         or email.lower() == "exit":
    exit()
  email_verifecation = input("Please verify your email : ")
  if email_verifecation.lower() == "quit" \
        or email_verifecation.lower() == "exit":
    exit()      

print("OK. You're in the club!")

sheety.post_new_row(first_name, last_name, email)