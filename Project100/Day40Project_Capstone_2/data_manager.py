import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/281c459fd63d9fbc2798cb8c4c5d3fda/flightDeals/prices"
SHEETY_USERS_ENDPOINT ="https://api.sheety.co/281c459fd63d9fbc2798cb8c4c5d3fda/flightDeals/user"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        sheety_response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            body = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            header = {
                "Content-Type": "application/json",

            }
            sheety_update = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=body, headers=header)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data