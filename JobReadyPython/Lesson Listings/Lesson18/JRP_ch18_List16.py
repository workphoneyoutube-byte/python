# This file should not exist...
f = open("data/another_file.txt", "x") 
f.close()

# We created this file earlier...
f = open("data/test_file.txt", "x") 
f.close()
