import datetime

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

cinMain = ""

while cinMain != 'quit':
    cinMain = input("Enter year to check: ")
    if cinMain != 'quit':
        year = int(cinMain)
        result = is_leap_year(year)
        print(f"{year} is {'a leap year' if result else 'not a leap year'}")
