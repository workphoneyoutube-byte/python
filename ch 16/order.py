
# Burger Shop Order Module
# This module defines the Order class for managing customer orders in a burger shop.
from menu import burger, drink, side, combo
class Order:
    def __init__(self,name):
        self.name = name
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)

    def get_price(self):
        price = 0.0
        for item in self.items:
            price = price + item.get_price()
        return price
    
    def __str__(self):
        print("=" * 30)
        print("Here is a summary of your order: ")
        print("Order for " + self.name)
        print("-" * 30)
        for item in self.items:
            print("= " * len(item.get_name()))
            print(str(item))
            print("= " * len(item.get_name()))
        print("-" * 30)
        return "Total Orer Amount: $" + str(self.get_price())
        print("=" * 30)
    
    def display(self):
        print("=" * 30)
        print("Here is a summary of your order")
        print("Order for " + self.name)
        print("Here is a list of items in the order: ")
        
        for item in self.items:
            print("_" * 30)
            print(str(item))
            print("-" * 30)
            print("Total Order Amount :$" + str(self.get_price()))
            print("=" * 30)