import datetime

cinDay = input("Enter Day: ")
cinHour = input("Enter Hour: ")
cinMinutes = input("Enter Minutes: ")

timeA = datetime.datetime(2026,12,int(cinDay),int(cinHour),int(cinMinutes))

cinDayB = input("Enter Day: ")
cinHourB = input("Enter Hour: ")
cinMinutesB = input("Enter Minutes: ")
cinSecondsB = input("Enter Seconds: ")

timeC = timeA + datetime.timedelta(days = int(cinDayB), hours = int(cinHourB), minutes = int(cinMinutesB), seconds = int(cinSecondsB))

print(timeA)
print(timeC)

timeD = timeA - datetime.timedelta(days = int(cinDayB), hours = int(cinHourB), minutes = int(cinMinutesB), seconds = int(cinSecondsB))
print(timeD)

print("Addition: ")
print(timeC.day,"Day",timeC.hour,"Hours",timeC.minute,"Minutes",timeC.second,"Seconds")
print("Subtraction: ")
print(timeD.day,"Day",timeD.hour,"Hours",timeD.minute,"Minutes",timeD.second,"Seconds")