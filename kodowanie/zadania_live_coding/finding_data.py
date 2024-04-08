day_temps = {
    "day1": [20, 31, 19],
    "day2": [14, 10, 24],
    "day3": [28, 32, 23],
}
# comp = 0
# for day, temps in day_temps.items():
#     max_temp = max(temps)
#     if max_temp > comp:
#         comp = max_temp
#         result = day
#
# print(f"result: {result}")


result = max(day_temps, key=lambda day: max(day_temps[day]))
print(f"result: {result}")

