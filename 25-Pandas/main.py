import pandas

data = pandas.read_csv("weather_data.csv")

# # Dataframe = The whole sheet
# print(type(data))

# # Series = Columns
# print(type(data["temp"]))


# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)


# # Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# Mon_Temp_C = monday.temp
# Mon_Temp_F = (Mon_Temp_C * 1.8) + 32
# print(Mon_Temp_F)


# Create a Dataframe from Scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
