import datetime

print(datetime.datetime.now())

# add one day to the current datetime
d1 = datetime.datetime.now() + datetime.timedelta(days = 1) 
print(d1)

# subtract 4 weeks from the current datetime
d2 = datetime.datetime.now() - datetime.timedelta(weeks = 4) 
print(d2)

# add one hour to the current datetime
d3 = datetime.datetime.now() + datetime.timedelta(minutes = 60, hours=1) 
print(d3)
