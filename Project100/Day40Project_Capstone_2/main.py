import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from customer_database import CustomerDatabase

print("Welcome to Lisi Priya's Flight Club.")
print("We will find teh best flight deals and email you")
FIRST_NAME = input("What is your first name?\n")
LAST_NAME = input("What is your first name?\n")
EMAIL = input("What is your email address?\n")
EMAIL_TO_VERIFY = input("Enter your email address again.\n")

customer = CustomerDatabase()
database_entry = customer.database_entry(FIRST_NAME, LAST_NAME, EMAIL, EMAIL_TO_VERIFY)
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "MAA"
from_date = str((dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y"))
six_month_from_today = str((dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y"))



if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_date=from_date,
        to_date=six_month_from_today
    )

    if flight is None:
        continue

    users = data_manager.get_customer_emails()
    emails = [row["email"] for row in users]
    names = [row["firstName"] for row in users]

    if flight is not None and flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-" \
                  f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        # notification_manager.send_notification(message)
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}." \
               f"{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}." \
               f"{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)


