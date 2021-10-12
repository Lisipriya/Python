import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"
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
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_notification(
            price=flight.price,
            departure_city=flight.origin_city,
            departure_airport=flight.origin_airport,
            arrival_city=flight.destination_city,
            arrival_airport=flight.destination_airport,
            outbound_date=flight.out_date,
            inbound_date=flight.return_date
        )
