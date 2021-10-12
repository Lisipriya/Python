TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "3y7-l5SOrMu54FRB7YS9CxZhqEjTpKHb"


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_airport, destination_city, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.destination_city = destination_city
        self.out_date = out_date
        self.return_date = return_date
