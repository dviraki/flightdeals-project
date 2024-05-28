import smtplib

#-------------------------------- CONSTANTS --------------------------------#
MY_EMAIL = """Company email address"""
PASSWORD = """mail app password"""
EMAIL_PROVIDER = """Company email provider (gmail,yahoo, etc..)"""

#sent email
class NotificationManager:

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
