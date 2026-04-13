class food_item:
    def  __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
    def get_price(self):
        return self.price

class burger(food_item):
    def __init__(self,name,price):
        super(burger, self).__init__(name,price)
        self.condiments = []
    def add_condiment(self,condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)
    def __str__(self):
        s = super(burger, self).__str__()
        s = s + "Condiments:" + ", ".join(self.condiments)
        return s
