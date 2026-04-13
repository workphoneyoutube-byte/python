# Another calculator with Class

# BEG DEF
class SimpleCalculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self,num1, num2):
        return (int(num1) + int(num2))
        
    def subtract(self,num1,num2):
        return (int(num1) - int(num2))
        
    def multiply(self,num1,num2):
        return (int(num1) * int(num2))
        
    def divide(self,num1,num2):
        return (int(num1) / int(num2))
# END DEF

cinMenu = ""

while cinMenu != 'quit':
    print("The calculator requires two values.")
    num1 = input("Please enter the first value: ")
    num2 = input("Please enter the second value: ")
    
    cinMenu = input("Choose option: quit, add, subtract, multiply or divide: ")
    calc = SimpleCalculator(num1,num2)

    if cinMenu == 'add':
        print(calc.add(num1,num2))
    elif cinMenu == 'subtract':
        print(calc.subtract(num1,num2))
    elif cinMenu == 'multiply': 
         print(calc.multiply(num1,num2))
    elif cinMenu == 'divide':
        print(calc.divide(num1,num2))
    elif cinMenu == 'quit':
        print("Goodbye!")
        break
    else:
        print("I'm sorry, I can't do that Dave.")
   