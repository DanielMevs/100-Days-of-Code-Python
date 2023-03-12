# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas


# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# average = data["temp"].mean()
# print(average)

# max_temp = data["temp"].max()
# print(max_temp)


# - These two are equivalent
# print(data["condition"])
# print(data.condition)


# print(data[data['day'] == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data['day'] == 'Monday']
# print(monday.temp)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Anagela"],
#     "scores": [76, 56, 63]
# }

# data = pandas.DataFrame(data_dict)
# print(data)

data = pandas.read_csv("squirrel_count.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# print(grey_squirrels)
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("new_squirrel_count.csv")