import random
import smtplib
import datetime as dt

my_email = "priyasmtptest@gmail.com"
password = "as1234.,"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        rand_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="aplisipriya1998@gmail.com",
            msg=f"Subject:Hello Visnu\n\n{rand_quote}."
        )