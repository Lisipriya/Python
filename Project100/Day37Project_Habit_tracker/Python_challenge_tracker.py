from calendar import Calendar
from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox

windows = Tk()
windows.title("Python Journey")
windows.config(pady=20, padx=20)

USER_NAME = "aplisipriya"
TOKEN = "lisvi2411"
GRAPH_ID = "pythongraphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}.html"
TODAY = dt.now()
# #user creation
pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json= user_params)
graphical_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graphical_params = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "minutes",
    "type" : "float",
    "color": "sora"
}
#
# response = requests.post(url=graphical_endpoint, headers=headers, json=graphical_params)
# print(response.text)
def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_input.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=headers)
    user_input.delete(0, END)
    messagebox.showinfo(message="Pixel added.")


def delete_pixel():
    endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{format_date()}"
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="Pixel deleted.")


def update_pixel():
    endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{format_date()}"
    pixel_update = {
        "quantity": user_input.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_input.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")


cal = Calendar(windows, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)
duration = Label(text="Minutes:")
duration.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
user_input = Entry(width=10)
user_input.grid(row=1, column=2, sticky="w")
add = Button(text="Add", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="Update", command=update_pixel)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=delete_pixel)
delete.grid(row=2, column=2, pady=10, sticky="w")
web_open = Button(text="Show\nJourney", command=open_browser)
web_open.grid(row=2, column=3)

windows.mainloop()
