import os

file_name = input("Please enter a file name to check for: ")
if os.path.exists("data/"+file_name):
    print("The file exists.")
else:
    print("The file doesn't exist.")
