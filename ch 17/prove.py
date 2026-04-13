import datetime

cinDNY = input("First Year: ")
cinDNM = input("First Month: ")
cinDND = input("First Day: ")
cinDNH = input("First Hour: ")
cinDNMin = input("First Minutes: ")
cinDNS = input("First Second: ")

d_now = datetime.datetime(int(cinDNY),int(cinDNM),int(cinDND),int(cinDNH),int(cinDNMin), int(cinDNS))

cinDOY = input("Second Year: ")
cinDOM = input("Second Month: ")
cinDOD = input("Second Day: ")
cinDOH = input("Second Hour: ")
cinDOMin = input("Second Minutes: ")
cinDOS = input("Second Seconds: ")

d_other = datetime.datetime(int(cinDOY),int(cinDOM),int(cinDOD),int(cinDOH),int(cinDOMin),int(cinDOS))

print(d_now)
print(d_other)

days_passed = d_now - d_other
print(days_passed)
print(days_passed.days)