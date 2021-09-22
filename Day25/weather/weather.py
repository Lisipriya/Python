# One method of getting columns from csv file
import csv


with open("weather_data.csv") as weather:
    data = csv.reader(weather)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    # Printing the temperature except the first item i.e "temp"
    print(temperatures[1:])

import pandas
data = pandas.read_csv("weather_data.csv")
# one way to find average
data_list = data["temp"].tolist()
average = round(sum(data_list)/len(data_list))
print(average)

# two way to find average
print(data["temp"].mean())
print(data["temp"].max()) or print(data.temp.max())

#print the row of items 2 ways
print(data[data.temp == data["temp"].max()])
print(data[data.day == "Monday"])
tuesday = data[data.day == "Tuesday"]
temperature_tuesday = tuesday.temp
in_fahrenheit = temperature_tuesday * 1.8 + 32
print(in_fahrenheit)

#creating new data frame and convert to csv file
data_dict = {
    "Students": ["Lisi", "Visnu", "Adhiyan"],
    "Score": [99, 90, 100]
}

data = pandas.DataFrame(data_dict)
data.to_csv("students.csv")
