import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 9.999670
MY_LONG = 77.619530
from_email = "priyasmtptest@gmail.com"
password = "as1234.,"
to_email = "aplisipriya1998@gmail.com"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour
    if hour_now >= sunset or hour_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=f"Subject:Hey Look up 🛰️\n\nThere is ISS roaming around you."
            )
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



