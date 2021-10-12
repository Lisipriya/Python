import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "3y7-l5SOrMu54FRB7YS9CxZhqEjTpKHb"
headers = {"apikey": TEQUILA_API_KEY}

class FlightSearch:
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        parameter = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=parameter)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, ORIGIN_CITY_IATA, destination, from_date, to_date):
        search_params = {
            "fly_from": ORIGIN_CITY_IATA,
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=search_params, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: ₹{flight_data.price}")
        return flight_data
