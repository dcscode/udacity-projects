# A bot to take food orders

import time

options = ["breakfast","brunch","lunch","snack","dinner","dessert"]

def print_timer(string):
	print(string)
	time.sleep(2)

def valid_order(prompt, options):
	while True:
		order = input(prompt).lower()
		for option in options:
			if option in order:
				return order
			else:
				print_timer("I do not understand.")

def greeting():
	print_timer("Hi, I'm Food Bot.")
		
def get_order():
	meal = valid_order("What meal are you having?\n", options)
	if "breakfast" in meal:
		print_timer("What would you like for breakfast?\n")
	elif "lunch" in meal:
		print_timer("What would you like for lunch?\n")
	elif "dinner" in meal:
		print_timer("What would you like for dinner?\n")
	elif "snack" in meal:
		print_timer("What would you like to have for a snack?\n")
	else:
		print_timer("I do not understand.\n")
	print_timer("Your order has been placed.")
	another_order()
	
	
def another_order():
	answer = ["yes","no"]
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
	



