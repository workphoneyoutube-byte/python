 # ERP Banking App

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
