numbers = [1,2,-1,6,-5,-2]

positive = []
negative = []

positive = [number for number in numbers if number>=0]
negative = [number for number in numbers if number<0]

print(positive)
print(negative)
