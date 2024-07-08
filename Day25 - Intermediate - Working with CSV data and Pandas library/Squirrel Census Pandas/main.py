
# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperature_list = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperature = int(row[1])
#             temperature_list.append(temperature)
#     print(temperature_list)

# # Using pandas library
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print("\n")
# print(data["temp"])

# data_dictionary = data.to_dict()
# print(data_dictionary)
#
# temperature_list = data["temp"].to_list()
# print(temperature_list)
#
# # Calculate average of the temperatures
# temp_sum = 0
# num_of_data = 0
# for temp in temperature_list:
#     temp_sum += temp
#     num_of_data += 1
# average_temp = temp_sum/num_of_data
# print(average_temp)
#
# average = sum(temperature_list)/len(temperature_list)
# print(average)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # Access columns
# print(data["condition"])
# print(data.condition)

# # Access rows
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# # Creating DataFrame from scratch
#
# test_dictionary = {
#     "subject": ["math", "science", "social", "biology"],
#     "scores": [79, 89, 90, 99]
# }
# data = pandas.DataFrame(test_dictionary)
# print(data)
# data.to_csv("new_data.csv")



# Working with central park squirrel census
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

dataframe = pandas.DataFrame(data_dictionary)
dataframe.to_csv("squirrel_data.csv")
