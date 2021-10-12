from pprint import pprint

import requests
import datetime as dt
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "3y7-l5SOrMu54FRB7YS9CxZhqEjTpKHb"
CITY_FROM = "LONDON"
parameter = {
            "term": CITY_FROM,
            "location_types": "city"
        }
headers = {"apikey": TEQUILA_API_KEY}
response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=parameter)
results = response.json()["locations"]
code = results[0]["code"]
# print(code)
today = dt.datetime.now()
from_date = str(today.strftime("%d/%m/%Y"))
to_date = str((dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y"))
# flight_params  = {
#     "fly_from": code,
#     "fly_to": "PAR",
#     "date_from": from_date,
#     "date_to": to_date,
#     "flight_type": "round",
#     "curr": "INR"
# }
# response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=flight_params)
# flight_price = response.json()
# pprint(flight_price)
search_params = {
    "fly_from": code,
    "fly_to": "PAR",
    "date_from": from_date,
    "date_to": to_date,
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "INR",
}

data = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=search_params, headers=headers)
flight_data = data.json()['data'][0]
price = flight_data['price']
pprint(price)