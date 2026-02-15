class Person:
    def __init__(self,fname,lname): 
        self.first_name = fname
        self.last_name = lname
    def display(self): 
        print("Person First Name: " + self.first_name)
        print("Person Last Name: " + self.last_name)

class Employee(Person):
    def __init__(self,emp_id,fname,lname):
        Person.__init__(self,fname,lname) 
        self.employee_id =emp_id
    def display(self):
        print("Employee ID: " + self.employee_id)
        print("Employee First Name: " + self.first_name)
        print("Employee Last Name: " + self.last_name)

class Director(Employee):
    def __init__(self,emp_id,fname,lname,d_level):
        # do not change this code
        Employee.__init__(self,emp_id,fname,lname)
        self.director_level = d_level
        self.team = list()
    def display(self):
        # a method that displays all the attributes of a director object
        pass
    def add_employee(self,emp):
        # a method to add an employee object to the team attribute 
        pass

class HourlyEmployee(Employee):
    # implement this  class
    pass


# DO NOT CHANGE THIS CODE 
d1 = Director("E24523525","Haythem","Balti","D-LEVEL-1")

# create first employee object 
e1 = Employee("E4746456456","Mark","Smith")
# add employee e1 to the team attribute of the Director class 
d1.add_employee(e1)
# create second hourlyemployee object 
e2 = HourlyEmployee("E47464578978","Mary","Lang")
# add hourly employee e2 to the team attribute of the Director class 
d1.add_employee(e2)

d1.display()
