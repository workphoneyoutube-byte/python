def compute_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total        

numbers = 1,5,5,7,10,1
summation = compute_sum(*numbers)
print(summation) 
