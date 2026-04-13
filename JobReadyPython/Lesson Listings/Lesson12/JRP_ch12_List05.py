# Name: Firstname Lastname
# Date created: Current date
# Purpose: Code-along for Python course

user_address = input("Enter an address (e.g., 123 Main Street): ")
if user_address.strip(): #check that string is not empty (afer removing leading
                         #and trailing spaces)
    print("Your address is " + user_address)
    split_address = user_address.split()
    print(split_address)   # temporary instruction to verify the list
The output should look like:
Enter an address (e.g., 123 Main Street or 425 Blue Boulevard): 789 Bradford Street
Your address is 789 Bradford Street
['789', 'Bradford', 'Street']
