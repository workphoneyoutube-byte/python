# Five seconds into the future
# Write a program that adds five seconds to the current time and displays the result

import datetime

today = datetime.datetime.now()

future = today + datetime.timedelta(seconds = 5)
print("Current time: " + str(today))
print("Five seconds later: " + str(future))