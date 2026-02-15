def find_div(transactions,factor):
    for num in transactions:
      if (num % factor == 0):
        print(num)

transactions = [1,5,5,7,10,1,9,12]
print("Factor of 3:") 
find_div(transactions,3) # find all transactions divisible by 3
print("Factor of 2:") 
find_div(transactions,2) # find all transactions divisible by 2
