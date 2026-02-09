# Print Dates: Yesterday, today and tomorrow

import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)

print("Yesterday: " + str(yesterday))
print("Today: " + str(today))
print("Tomorrow: " + str(tomorrow))
