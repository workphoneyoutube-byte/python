def find_greater(numbers,threshold):
    for num in numbers:
        # we only display the numbers that are above the input threshold
        if (num > threshold):
            print(num)

numbers = [1,5,5,7,10,1]
find_greater(numbers,0) # find all numbers greater than 0
print("----")
find_greater(numbers,5) # find all numbers greater than 5
