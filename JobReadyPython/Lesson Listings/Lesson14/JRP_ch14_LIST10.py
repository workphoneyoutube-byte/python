class MathFormula:
    @staticmethod
    def display(message):
        print(message)
    @staticmethod
    def pow(x,y):
        return x**y
    @staticmethod
    def isEven(x):
        if x%2==0:
            return True
        return False
        

MathFormula.display("hello")
MathFormula.display("world")
MathFormula.display (MathFormula.pow(3,2))
