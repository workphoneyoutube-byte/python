# Display the following:
# Current date and time
# Current year
# Current month
# week number of the year
# weekday of the week
# day of the year
# day of the month
# day of the week

import datetime

d = datetime.datetime.now()
print(f"Current date and time: {d}")

d_str = str(d)
(date_part,time_part) = d_str.split()
(year,month,day) = date_part.split("-")

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day of month: {day}")

print(f"Week number of the year: {d.isocalendar()[1]}")
print(f"Weekday of the week: {d.weekday()}")
print(f"Day of the year: {d.timetuple().tm_yday}")
print(f"Day of the month: {d.day}")
print(f"Day name: {d.strftime('%A')}")
