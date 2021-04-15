# A bot to take food orders

import time

options = ["breakfast","brunch","lunch","snack","dinner","dessert"]

breakfast = ["eggs","toast","waffle","hashbrowns"]

lunch = ["sandwich","salad","tacos","burritos","pizza","soup"]

mealtimes = [breakfast, lunch]

def print_timer(string):
	print(string)
	time.sleep(2)

def valid_meal(prompt, options):
    while True:
	    meal = input(prompt).lower()
	    for option in options:
		    if option in meal:
			    return meal
	    print_timer("I do not understand.")
    
def valid_order(prompt, mealtimes):
    while True:
        order = input(prompt).lower()
        for food in mealtimes:
            if food in order
                return order
        print_timer("I do not understand.")

def greeting():
	print_timer("Hi, I'm Food Bot.")
		
def get_order():
	meal = valid_meal("What meal are you having?\n", options)
	if meal in options:
		order = valid_order("What would you like for " + meal + "?\n", mealtimes)
        if order in mealtimes:
            print_timer("Your order has been placed.")
	    else:
		    print_timer("I do not understand.\n")
	another_order()
	
	
def another_order():
	answer = ["yes","no"]
	another_meal = valid_meal("Would you like to place another order?\n",answer)
	if "no" in another_meal:
		print_timer("Have a nice day!\n")
	if "yes" in another_meal:
		print_timer("I can take your order.\n")
		get_order()

def order_food():
	greeting()
	get_order()

order_food()
	



