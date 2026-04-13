# Name: Firstname Lastname
# Date created: Current date
# Purpose: Code-along for Python course

user_address = input("Enter an address (e.g., 123 Main Street): ")
if user_address.strip(): #check that string is not empty (afer removing leading
                         #and trailing spaces)
    print("Your address is " + user_address)
