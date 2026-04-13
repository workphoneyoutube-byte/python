# 15.1 - 15.5 
# BEGDEF
class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def display(self):
        print(self.first_name + " " + self.last_name)
        print("Person First Name: " + self.first_name)
        print("Person Last Name: " + self.last_name)

# Create employee class that inherits from person class.
class Employee(Person):
    def __init__(self,name_in,loc):
        self.name = name_in
        self.location = loc
    def display (self):
        print("Employee name: " + self.name)
        print("Employee location: " + self.location)

class Teller(Employee):
    pass

class Director(Employee):
    def __init__(self,emp_id,fname,lname,d_level):
        Employee.__init__(self,emp_id,fname,lname)
        self.director_level = d_level
# ENDDEF

d1 = Director("E240902","John","Smith","D-LEVEL-1")
d1.display()
print("Employee ID: " + d1.employee_id)
print("Director Level: " + str(d1.director_level))

print("------")

d2 = Director("E240903","Jane","Doe","D-LEVEL-5")
d2.display()
print("Employee ID: " + d2.employee_id)
print("Director Level: " + str(d2.director_level))

x = Person("Asia", "Roberson")
x.display()

# 15.6
class Employee:
    def __init__(self,n,i):
        self.name = n 
        self.id = i
    def display(self):
        print("Employee name is: " + self.name)
        print("Employee ID is: " + self.id)

class Manager(Employee):
    def __init__(self,t,n,i,):
        Employee.__init__(self,n,i)
        self.team = t
        self.id = i 
    def display(self):
        print("Manager's employee ID is: " + self.id)
        print("Manager's name is: " + self.name)
        print("Manager's team is: " + self.team)

m1 = Manager("RobertA, La Terrance S", "Julia Juares","A1208949")
m2 = Manager("Liyana J, Angeline P", "Whitney Solomon", "A190805")
m1.display()
m2.display()

class Teller(Employee):
    def __init__(self,b,n,i):
        Employee.__init__(self,n,i)
        self.bank_branch = b
    def display(self):
        print("Teller's employee ID is: " + self.id)
        print("Teller's name is: " + self.name)
        print("Teller's bank branch is: " + self.bank_branch)

t1 = Teller("Columbia Ave. ", "Lamar Mercer", "A10902049")
t2 = Teller("Constitution Dr.","Karly Robinson","A2094209")
t1.display()
t2.display()

class CustomerServRep(Employee):
    def __init__(self,c,n,i):
        Employee.__init__(self,n,i)
        self.call_center = c
    def display(self):
        print("Customer Service Rep's employee ID is: " + self.id)
        print("Customer Service Rep's name is  " + self.name)
        print("Customer Service Rep's call center is: " + self.call_center)
    
cs1 = CustomerServRep("Headquarters", "Clayton Ryan", "A129409099")
cs2 = CustomerServRep("Headquarters", "Gage Barnett", "A930930293")
cs1.display()
cs2.display()