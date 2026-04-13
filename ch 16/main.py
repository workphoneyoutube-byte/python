# Burger Shop Main Module
# This module serves as the entry point for the burger shop application.
from order import Order
from menu import burger, drink, side, combo

# CONSTANTS
BURGER_PRICE = 6.00
BURGER_CONDIMENTS = ['Ketchup', 'Mustard', 'Mayo', 'Lettuce', 'Tomato', 'Onion', 'Pickles']
DRINK_TYPES = ['Fanta', 'Coke', 'Sprite', 'Root Beer']
DRINK_SIZES = [12,16,20]
DRINK_PRICES = [2.00, 2.50, 3.00]
SIDES = ['Fries', 'Onion Rings', 'Salad']
SIDE_PRICE = 2.50
COMBO_DISCOUNT = 1.50

def order_many():
    print("Welcome to San Diego Burger Shop!")
    customer = input("Please enter the customer name: ")
    order = Order(customer)
    print("Starting new order for " + customer)
    done = False
    while done == False:
        item = order_once()
        order.add_item(item)
        customer = input("Do you need more items? (Enter n to stop.) ")
        if customer.lower() == 'n':
            done = True
    return order

def order_once():
    possible_options = [1,2,3,4]
    print("Type 1 for a Burger.")
    print("Type 2 for a Drink.")
    print("Type 3 for a Side.")
    print("Type 4 for a Combo.")
    choice = None
    while choice == None:
        q1 = input("Please enter your choice: ")
        if int(q1) in possible_options:
            choice = int(q1)
    item = None
    if choice == 1:
        item = get_burger_order()
    elif choice == 2:
        item = get_drink_order()
    elif choice == 3:
        item = get_side_order()
    elif choice == 4:
        item = get_combo_order()
    return item

# Functions to get specific item orders
def get_burger_order():
    b = burger("Burger", BURGER_PRICE)
    customer = input("Would you like condiments on your burger? (y/n) ")
    if customer.lower() == 'y':
        for condiments in BURGER_CONDIMENTS:
            want_condiment = input("Would you like " + condiments + "? (y/n) ")
            if want_condiment.lower() == 'y':
                b.add_condiment(condiments)
    return b

def get_drink_order():
    print("These are the available drinks: ")
    print(DRINK_TYPES)
    print("These are the available sizes: ")
    print(DRINK_SIZES)
    choice = False
    drink_name = None
    drink_size = 0
    drink_price = None 
    while choice == False:
        print(DRINK_TYPES)
        q1 = input("What drink do you want? ")
        if q1.title() in DRINK_TYPES:
            choice = True
            drink_name = q1.title()
        else:
            print("Please enter a valid drink. ")
    choice = False

    while choice == False:
        q1 = input("What size do you want? " + str(DRINK_SIZES) + ": ")
        if int(q1) in DRINK_SIZES: 
            choice = True
            drink_size = int(q1)
        else:
            print("Please enter a valid size. ")
    
    # locate the price of the drink base on the index of the size:
    drink_price = DRINK_PRICES[DRINK_SIZES.index(drink_size)]
    d = drink(drink_name, drink_size,drink_price)
    return d

def get_side_order():
    print("These are the available sides: ")
    print(SIDES)
    choice = False
    side_name = None
    while choice == False: 
        q1 = input("Please enter your side choice: ")
        if q1.title() in SIDES:
            choice = True
            side_name = q1.title()
        else:
            print("Please enter a valid side.")
    s = side(side_name,SIDE_PRICE)
    return s

def get_combo_order():
    print("Let's get you a combo meal!")
    print("First, let's order the burger for your combo.")
    b = get_burger_order()
    print("Now, let's order the drink for your combo.")
    d = get_drink_order()
    print("Finally, let's order the side for your combo..")
    s = get_side_order()
    c = combo("Combo",b,d,s,COMBO_DISCOUNT)
    return c

client_order = order_many()
client_order.display()
