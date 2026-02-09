# Build Time Duration Calculator
# It will Add or Subtract two different lengths of time
# Must include: days, hours, minutes and seconds
# User prompt - Must allow specification of addition or subtraction
# User specification must be between two different input times
# Multiple Outputs Include the Following: 
# Number of days, hours, minutes and seconds
# Number of days
# Number of hours
# Number of minutes
# Number of seconds

import datetime

class TimeDuration:
    def __init__(self,days,hours,minutes,seconds):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def timeAdd(self,days,hours,minutes,seconds):
        TimeDuration.__init__(days,hours,minutes,seconds)
        return datetime.timedelta(days,hours,minutes,seconds).timestamp()

a = TimeDuration(1,0,0,0)
b = TimeDuration(1,0,0,0)

c = int(a) + int(b)
print(c)