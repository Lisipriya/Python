from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "priyasmtp"
TOKEN = "aqswdefr.,1234"
GRAPH_ID = "graph"
HEADER = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

graphical_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"


graphical_params = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "minutes",
    "type" : "float",
    "color": "sora"
}

# response = requests.post(url=graphical_endpoint, headers=HEADER, json=graphical_params)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
pixel_data = {
    "date": formatted_date,
    "quantity": "40"
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=HEADER)
# print(response.text)

# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# update_params = {
#     "quantity": "120"
# }
# response = requests.post(url=update_pixel_endpoint, json=update_params, headers=HEADER)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "120"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=HEADER)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20200810"

response = requests.delete(url=delete_endpoint, headers=HEADER)
print(response.text)
