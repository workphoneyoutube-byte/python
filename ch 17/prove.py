import datetime

cinDay = input("Enter Day: ")
cinHour = input("Enter Hour: ")
cinMinutes = input("Enter Minutes: ")
#cinSeconds = input("Enter Seconds: ")

#timeA = datetime.datetime(int(cinDay),int(cinHour),int(cinMinutes),int(cinSeconds))

timeA = datetime.datetime(2026,12,int(cinDay),int(cinHour),int(cinMinutes))

cinDayB = input("Enter Day: ")
cinHourB = input("Enter Hour: ")
cinMinutesB = input("Enter Minutes: ")
#cinSecondsB = input("Enter Seconds: ")

#timeB = datetime.datetime(int(cinDayB),int(cinHourB),int(cinMinutesB),int(cinSecondsB))

# add one hour to the current datetime
# d3 = timeA + datetime.timedelta()

#timeC = timeA + datetime.timedelta(days = int(cinDayB), hours = int(cinHour), minutes = int(cinMinutes), seconds = int(cinSeconds))

timeC = timeA + datetime.timedelta(days = int(cinDayB), hours = int(cinHourB), minutes = int(cinMinutes))
timeD = timeA - datetime.timedelta(days = int(cinDayB), hours = int(cinHourB), minutes = int(cinMinutes))

print("Addition: ")
print(timeC.day,timeC.hour,timeC.minute,timeC.second)
print("Subtraction: ")
print(timeD.day,timeD.hour,timeD.minute,timeD.second)