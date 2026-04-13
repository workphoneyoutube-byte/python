# Listing 15.7
#BEGDEF
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
        self.employee_id = emp_id
    def display(self):
        print("Employee ID: " + self.employee_id)
        print("Employee First Name: " + self.first_name)
        print("Employee Last Name: " + self.last_name)

class Director(Employee):
    def __init__(self,emp_id,fname,lname,d_level,team):
        # do not change this code
        Employee.__init__(self,emp_id,fname,lname)
        self.director_level = d_level
        self.team = list()

# Add attribute to Director class called Team
# Team represents the employees that the director manages
# Team should be a list of Employee objects

    def display(self):
        # a method that displays all the attributes of a director object 
        print("Director ID: " + self.employee_id)
        print("Director First Name: " + self.first_name)
        print("Director Last Name: " + self.last_name)
        print("Director Level: " + self.director_level)
        print("Director team is: " + str(self.team))
              
    def add_employee(self,emp):
        # a method that add an employee object to the team attribute
        self.employ_id = emp
        self.team.append(str(self.employ_id))


class HourlyEmployee(Employee):
    def __init__(self,emp_id,fname,lname,h_rate,h_hours,team):
        Employee.__init__(self,emp_id,fname,lname)
        self.hourly_rate = h_rate
        self.hours_worked = h_hours
        self.team = team
    def calculate_pay(self):
        # a method that calculates the pay of an hourly employee
        rate = 20
        hr = 1
        pay = hr * rate
    def display(self):
        # a method that displays all the attributes of an hourly employee
        print("Hours worked: " + self.hours_worked)
        print("Hourly rate: " + self.hourly_rate)
#ENDDEF



# DO NOT CHANGE THIS CODE

d1 = Director("E24209502", "Haythem", "Balti", "D-LEVEL-1",team=[])
d1.display() # no team members

e1 = Employee("E24209503","Mark","Smith")

# add employee e1 to the team attribute of the Director class 
d1.add_employee(e1.employee_id)

# Team members added to D1
d1.display()

# create second hourly employee object
e2 = HourlyEmployee("E24209504","Mary","Lang","25","40","E")
e3 = HourlyEmployee("E20294939","John","Wick","40","99","E")

# add hourly employee e2 to the team attribute of the Director class
d1.add_employee(e3.employee_id)
d1.add_employee(e2.employee_id)
# Hourly employees added to Team
d1.display()

