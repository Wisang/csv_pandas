import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"]

gray = 0
cinnamon = 0
black = 0

for color in colors.to_list():
    if color == "Gray":
        gray += 1
    if color == "Cinnamon":
        cinnamon += 1
    if color == "Black":
        black += 1


data_dict = {
    "colors": ["gray", "cinnamon", "black"],
    "counts": [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel count.csv")