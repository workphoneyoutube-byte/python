# Classy Vehicles

# beg def

class ClassyVehicles:
    def __init__(self, make, model, type, year, color):
        self.car_Make = make
        self.car_Model = model
        self.car_Type = type
        self.car_Year = year
        self.car_Color = color
        
    def display_info(self):
        """
        Purpose: Print out class documentation to console out
        """
        print("The make of this car: " + self.car_Make)
        print("The model of this car: "  + self.car_Model)
        print("The car type is: " + self.car_Type)
        print("The car was built in: " + self.car_Year)
        print("The color of the car is: " + self.car_Color)
    
    # end def
    
sunday = ClassyVehicles("Bentley","Aviator","Soft Top","1926","Electric Blue")
monday = ClassyVehicles("Ford","Mustang","Mach 1","2002","Virgin Mary Blue")
    
sunday.display_info()
monday.display_info()