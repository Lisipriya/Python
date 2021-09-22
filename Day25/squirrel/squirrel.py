import pandas

squirrel_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
column_values = squirrel_file["Primary Fur Color"]
squirrel_list = column_values.tolist()
print(squirrel_list)
colors = {
    "Gray": 0,
    "Black": 0,
    "Cinnamon": 0
}
for color in squirrel_list:
    if color == "Gray":
        colors[color] += 1
    elif color == "Black":
        colors[color] += 1
    elif color == "Cinnamon":
        colors[color] += 1

squirrel_dataframe = pandas.DataFrame({'Fur color': colors.keys(), 'count': colors.values()})
squirrel_dataframe.to_csv("squirrel_count.csv")


# 2nd method
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
