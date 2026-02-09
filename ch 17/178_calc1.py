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

cinDays = 0
cinHours = 0
cinMin = 0
cinSec = 0

class timeDuration:
    def timeA(self,cinDays,cinHours,cinMin,cinSec):
        self.daysa = cinDays
        self.hoursa = cinHours
        self.mina = cinMin
        self.seca = cinSec

        return datetime.timedelta(days = self.daysa, hours = self.hoursa, minutes = self.mina, seconds 
        = self.seca)

    def timeB(self,cinDays,cinHours,cinMin,cinSec):
        self.daysb = cinDays
        self.hoursb = cinHours
        self.minb = cinMin
        self.secb = cinSec
        
        return datetime.timedelta(days = self.daysb, hours = self.hoursb, minutes = self.minb, seconds = self.secb)

a = timeDuration()
b = timeDuration()

# example values — replace or wire up inputs as needed
c = a.timeA(1, 1, 1, 1) + b.timeB(1, 1, 1, 1)
