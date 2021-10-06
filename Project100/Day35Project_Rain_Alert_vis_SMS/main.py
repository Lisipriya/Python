import requests
from twilio.rest import Client

MY_API_KEY = "7f58027c84146316fbdbb63dbb777317"
MY_LAT = 9.999670
MY_LONG = 77.619530
URL = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC10089714966288b5f25d4475dcf470c3"
auth_token = "ddf6029b9054341c31f5a973a00f202a"
FROM_NUM = "+16513722177"
# twilio_pwd = "asdflk123456789.,"


parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": MY_API_KEY,
        "exclude": "current,minutely,daily"
    }

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
twelve_hour_data = data["hourly"][0:12]
will_rain = False

for codes in twelve_hour_data:
    weather_code = codes["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="\nHey Lisi Priya here\n It is going to rain today\nRemember to take an umbrella ☔",
        from_=FROM_NUM,
        to="+919865575106"
    )

    print(message.status)
