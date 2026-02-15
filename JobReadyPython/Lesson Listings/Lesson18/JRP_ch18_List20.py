import os

os.remove("data/test_file.txt") # Deleting file from previous example. 
print("The file test_file.txt deleted successfully.")

# The following file doesn’t exist, so will cause error!
os.remove("data/missing_file.txt") 
print("The file missing_file.txt deleted successfully.")
