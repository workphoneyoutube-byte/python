# 18.1 simple file i/o script
f = open("JobReadyPython/data/flatland01.txt", "r")
print(f.readline())
f.close()

# 18.2 opening a file called flatland01.txt

# Open our file in read mode
f = open("JobReadyPython/data/flatland01.txt", mode="r")
print(f.read())

# close our file resource
f.close()

# 18.3 Reading the contents of a text file
class flatland:
    f = open("JobReadyPython/data/flatland01.txt", mode = "r")
    text = f.read()
    print(text)
    f.close()

# 18.4 Limiting the amount read
f = open("JobReadyPython/data/flatland01.txt", "r")
print(f.read(100)) # This will pull the first 100 characters 
f.close()   