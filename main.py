# import csv
#
# with open("weather_data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperature = []
#     for row in weather_data:
#         temperature.append(row[1])
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
