from twilio.rest import Client

account_sid = "AC10089714966288b5f25d4475dcf470c3"
auth_token = "4bc9d93615a1f9919d22d9f1b05586fe"
FROM_NUM = "+16513722177"
TO_NUM = "+919865575106"

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, price, departure_city, departure_airport, arrival_city,
                          arrival_airport, outbound_date, inbound_date):

        message = self.client.messages.create(
            body=f"\nLow Price Alert\n Only ₹{price} to fly from {departure_city}-{departure_airport} to "
                 f"{arrival_city}-{arrival_airport} from {outbound_date} to {inbound_date}",
            from_=FROM_NUM,
            to=TO_NUM
        )

        print(message.sid)

