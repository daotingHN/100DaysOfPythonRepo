# Fur Color, Count
# Primary Fur Color = ["Gray", "Cinnamon", "Black"]

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_total = data["Primary Fur Color"]


# # Primitive Solution
# gray_count = 0
# red_count = 0
# black_count = 0
#
# for squirrel in color_total:
#     if squirrel == "Gray":
#         gray_count += 1
#     if squirrel == "Cinnamon":
#         red_count += 1
#     if squirrel == "Black":
#         black_count += 1


# Optimized Solution
gray_count = len(data[color_total == "Gray"])
red_count = len(data[color_total == "Cinnamon"])
black_count = len(data[color_total == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}
squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")
