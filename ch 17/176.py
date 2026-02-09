# Setting Future Days
# Write a program that prints the date for the next five days
# Starting from today

import datetime

today = datetime.datetime.now()

for i in range(1,6):
    date = today + datetime.timedelta(days = i)
    print(date)