import random
import smtplib

import pandas
import datetime as dt
##################### Extra Hard Starting Project ######################
my_email = "priyasmtptest@gmail.com"
password = "as1234.,"

today = dt.datetime.now()
month_now = today.month
day_now = today.day
today = (month_now, day_now)

birth_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in birth_data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    name = birthday_person["name"].strip()
    email = birthday_person["email"].strip()
    with open(file_path) as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Hello {name}\n\n{new_letter} This is my first automated email sending program."
            )





