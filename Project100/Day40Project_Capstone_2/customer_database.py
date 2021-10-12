import requests

sheety_url ="https://api.sheety.co/281c459fd63d9fbc2798cb8c4c5d3fda/flightDeals/user"


class CustomerDatabase:
    def database_entry(self, firstname, lastname, email, email_to_verify):

        while email != email_to_verify:
            email_to_verify = input("You have typed the wrong email address\nEnter your email address again.\n")
        print("You have joined Lisi Priya's Flight Club successfully ✈️")

        header = {
            "Content-Type": "application/json",
        }

        body = {
          "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
          }
        }

        sheety_response = requests.post(
        url=f"{sheety_url}",
        json=body,
        headers=header
        )

