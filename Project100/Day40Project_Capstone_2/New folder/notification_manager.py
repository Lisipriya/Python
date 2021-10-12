import smtplib
from twilio.rest import Client


TWILIO_SID = "AC10089714966288b5f25d4475dcf470c3"
TWILIO_AUTH_TOKEN = "4bc9d93615a1f9919d22d9f1b05586fe"
TWILIO_VIRTUAL_NUMBER = "+16513722177"
TWILIO_VERIFIED_NUMBER = "+919865575106"
MY_EMAIL = "priyasmtptest@gmail.com"
MY_PASSWORD = "asdflk123456789.,"
to_email = "aplisipriya1998@gmail.com"
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )