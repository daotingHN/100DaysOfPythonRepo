# days_weather = []
#
# with open("weather_data.csv", mode="r") as weather_file:
#     days = weather_file.readlines()
#
#     for day in days:
#         day_stripped = day.strip()
#         days_weather.append(day_stripped)
#
# days_weather.pop(0)
#
# print(days_weather)


# import csv
#
# with open("weather_data.csv", mode="r") as weather_file:
#     days = csv.reader(weather_file)
#     temperature = []
#
#     for row in days:
#         # print(row)
#
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
