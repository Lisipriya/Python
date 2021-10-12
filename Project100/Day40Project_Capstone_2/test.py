import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "3y7-l5SOrMu54FRB7YS9CxZhqEjTpKHb"
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/281c459fd63d9fbc2798cb8c4c5d3fda/flightDeals/prices"

headers = {"apikey": TEQUILA_API_KEY}

parameter = {
            "term": "Madurai",
            "location_types": "city"
        }
response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=parameter)
results = response.json()["locations"]
code = results[0]["code"]
print(code)
search_params = {
            "fly_from": code,
            "fly_to": "HYD",
            "date_from": "13/10/2021",
            "date_to": "01/01/2022",
            # "nights_in_dst_from": 7,
            # "nights_in_dst_to": 28,
            "flight_type": "oneway",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR",
        }

response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=search_params, headers=headers)

print(response.json()["data"][0]["price"])