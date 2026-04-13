class Calculator:
    def __init__(self,num1,num2):
        self.value1 = num1
        self.value2 = num2
    
    def add(self,num1,num2):
        return num1 + num2
    
calc = Calculator(1,1)

print(calc.add(1,1))