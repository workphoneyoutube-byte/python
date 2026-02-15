import datetime

# Creates a new variable using todays date
dateA = datetime.datetime.now()

# Takes user input and stores in memory
cinDays = input("Enter Day: ")
cinHours = input("Enter Hour: ")
cinMinutes = input("Enter Minutes: ")
cinSeconds = input("Enter Seconds: ")

# creates second date using input
timeA = datetime.datetime(2026,12,int(cinDays),int(cinHours),int(cinMinutes),int(cinSeconds))

# Secondary  input
cinDaysB = input("Enter Day: ")
cinHoursB = input("Enter Hour: ")
cinMinutesB = input("Enter Minutes: ")
cinSecondsB = input("Enter Seconds: ")

# Calculates time
timeC = timeA + datetime.timedelta(days = int(cinDaysB), hours = int(cinHoursB), minutes = int(cinMinutesB), seconds = int(cinSecondsB))

timeC2 = datetime.timedelta(days = int(cinDays), hours = int(cinHours), minutes = int(cinMinutes), seconds = int(cinSeconds)) + datetime.timedelta(days = int(cinDaysB), hours = int(cinHoursB), minutes = int(cinMinutesB), seconds = int(cinMinutesB))

print(timeA)
print(timeC)
print(timeC2)

timeD = timeA - datetime.timedelta(days = int(cinDaysB), hours = int(cinHoursB), minutes = int(cinMinutesB), seconds = int(cinSecondsB))
print(timeD)

print("Addition: ")
print(timeC.day,"Day",timeC.hour,"Hours",timeC.minute,"Minutes",timeC.second,"Seconds")
print("Subtraction: ")
print(timeD.day,"Day",timeD.hour,"Hours",timeD.minute,"Minutes",timeD.second,"Seconds")