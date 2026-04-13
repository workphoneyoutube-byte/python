# 14.1 Creating a Person object
class Person:
        # init method or constructor
        def __init__(self, name):
            self.name = name # name ios an instance attribute.and
p = Person("irrelevent")
print(p.name)

# 14.2 Person class with multiple attributes
class Person:
    
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

person_1 = Person("Lewis", "Montes")
print(person_1.first_name)
print(person_2.last_name)

person_2 = Person("Robin", "Durham")
print(person_2.first_name)
print(person_2.last_name)

# 14.3 adding a method to our Person class
class Person:
    def __init__(self, fname):
        self.first_name = fname 
        self.last_name = lname
    def display_info(self):
        print("Person First Name: " + self.first_name)
        print("Person Last Name: " + self.last_name)

person_1 = person("Lewis", "Montes")
person_1.display_info()

person_2 = Person("Robin", "Durham")
person_2.display_info()

# 14.4 using methods in our banking app

class BankCustomer:
    def __init__(self,c_id,fname,lname):
        self.first_Name = fname
        self.last_Name = lname
        self.customer_ID = c_id
    
    def display_info(self):
        print("Customer's first name is " + self.first_Name)
        print("Customer's last name is " + self.last_Name)
        print("Customer's ID is " + str(self.customer_ID))
        
class BankAccount: 
    def __init__(self,a_id,name,type):
        self.account_ID = a_id
        self.account_Name = name
        self.account_Type = type
    
    def display_info(self):
        print("The account name is " + self.account_Name)
        print("The account type is " + self.account_Type)
        print("Account ID is " + str(self.account_ID))

# setup customers        
customer1 = BankCustomer(100004, "Layla", "Brennan")
customer2 = BankCustomer(100005, "Moises", "Cardenas")
customer3 = BankCustomer(100006, "Maria", "Pierce")

# setup account
account1 = BankAccount(1004, "Layla's Account", "Checking")
    
customer1.display_info()
customer2.display_info()
customer3.display_info()    
account1.display_info()

    
# 14.5 classes to represent employees in our banking app
class Manager():
    def __init__(self, n, i, t):
        self.name = next
        self.id = i
        self.team = t

    def display(self):
        print("Manager name is: " + self.name)
        print("Manager ID is: " + self.id)
        print("Manager's team is: ")
        for member in self.team: 
            print(member)
            
class Teller():
    def __init__(self, n, i, b):
        self.name = n
        self.id = i
        self.bank_branch = b
        
    def display(self):
        print("Teller's employee ID is: " + self.id)
        print("Teller's name is: " + self.name)
        print("Teller's bankbranch is: " + self.bank_branch)
        
        
class CustomerServRep():
    def __init__(self, n, i, c):
        self.name = n
        self.id = i
        self.call_center = c
        
    def display(self):
        print("Customer Service Rep's employee ID is: " + self.id)
        print("Customer Service Rep's name is: " + self.name)
        print("Customer Service Rep's call center is " + self.call_center)
        
# Create managers
m1 = Manager("Julia Juarez", "A115226", ["Robert A", "LaTerrance S"])
m2 = Manager("Whitney Solomon", "A152243", ["Lilyana J", "Angeline P"])
m1.display()
m2.display()

# Create tellers
t1 = Teller("Lamar Mercer", "A115462", "Columbia Ave. ")
t2 = Teller("Karly Robinson","A2352346","Constitution Dr.")
t1.display()
t2.display()

# Create Customer Service Reps
cs1 = CustomerServRep("Clayton Ryan", "A346343", "Headquarters")
cs2 = CustomerServRep("Gage Barnett", "A3476093","Headquarters")
cs1.display()
cs2.display()

# 14.6 manager class with a class attribute 
class Manager:
    level = "L1" # this is a class attribute shared among all objects
    
    def __init__(self,fname,lname):
        self.fname = fname # instance attribute tied to the object
        self.lname = lname # isntance attribute tied to the object
        
    
p1 = Manager ("Haythem", "Balti")
print(p1.fname)
print(p1.level)

p2 = Manager("Kim","Weiss")
print(p2.fname)
print(p2.level)

# 14.7 using a class attribute in our account class
class CheckingAccount:
    type = "checking"
    def __init__(self,id,balance):
        self.account_id = id
        self.balance = balance
        
ch1 = CheckingAccount("ID3454", 123452)
ch2 = CheckingAccount("ID34632",959309)

print(ch1.type)
print(ch2.type)

# 14.8 math method
class MathFormula:
    def pow(self,x,y):
        return x**y
    
m = MathFormula()
print(m.pow(3,3))

# 14.9 static math method
class MathFormula:
    @staticmethod
    def pow(x,y):
        return x**y

print(MathFormula.pow(3,3))

# 14.10 more robust math class
class MathFormula:
    @staticmethod
    
    def display(message):
        print(message)
    
    @staticmethod
    
    def pow(x,y):
        return x**y
    @staticmethod
    
    def isEven(x):
        if x % 2 == 0:
            return True
        return False

# 14.11 sales class
class Sales:
    @staticmethod
    def applySalesTax(amount):
        sales_tax = 0.06
        return amount * (1 + sales_tax)
    @staticmethod
    def applySalesTaxMany(amounts):
        out = list()
        sales_tax = 0.06 
        out = [amount * (1 + sales_tax ) for amount in amounts]
        return out
    
# 14.12 using a class method
class Sales:
    sales_tax = 0.06
    @classmethod
    def applySalesTax(cls,amount):
        
        return amount * (1 + cls.sales_tax)
    
    @classmethod
    def applySalesTaxMany(cls,amounts):
        out = list()
        sales_tax = 0.06
        out = [amount * (1 + cls.sales_tax) for amount in amounts]
        return out
    
print(Sales.applySalesTax(20))
print(Sales.applySalesTaxMany([10,20,30]))
