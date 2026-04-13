f = open("data/flatland01.txt", "r")

for line in f:  # the file object can be iterated on at the line level. 
    print(line) # with each iteration, line contains the current line.

f.close()
