# A bot to take food orders

import time

food = ["burritos","tacos","quesadilla","pizza","grilled cheese"]

drinks = ["soda","horchata","water","tea"]

answer = ["yes","no"]

def print_timer(string):
	print(string)
	time.sleep(2)

def valid_order(prompt, order):
    while True:
	    order = input(prompt).lower()
	    for option in order:
		    if option in order:
			    return order
	    print_timer("I do not understand.")

def greeting():
	print_timer("Hi, I'm Food Bot." "Here is our menu:\n"
		    "Burrito"
		    "Tacos"
		    "Quesadilla"
		    "Pizza"
		    "Grilled Cheese\n")
def get_order():
	order = valid_order("What would you like to eat?\n", food)
	if order in food:
		drink = valid_order("Would you like a drink?\n"
				    "Soda"
				    "Horchata"
				    "Water"
				    "Tea/n", answer)
     	if "no" in drink:
			print_timer(order.capitalize() + ".")
		if "yes" in drink:
			drink = valid_order("What would you like to drink?\n", drinks)
			print_timer(order.capitalize() + " and a " + drink + ".")
       	print_timer("Your order has been placed.")
	else:
		print_timer("I do not understand.\n")
	another_order()
	
	
def another_order():
	another_meal = valid_order("Would you like to place another order?\n",answer)
	if "no" in another_meal:
		print_timer("Have a nice day!\n")
	if "yes" in another_meal:
		print_timer("I can take your order.\n")
		get_order()

def order_food():
	greeting()
	get_order()

order_food()
	



