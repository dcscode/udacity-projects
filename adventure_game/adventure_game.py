import time
import random
 
health = 50
enemy = 50
opponents = ["opponent 1", "opponent 2", "opponent 3", "opponent 4"]
def print_timer(string):
    print(string)
    time.sleep(1)
    

print_timer("You seek glory.")
print_timer("You have come to the arena to claim it.")

while True:
    choice = input("Enter 1 to visit the locker room.\nEnter 2 to step onto the field.\nWhich will you choose? (Please enter 1 or 2)\n")
    if choice == "1":
        print_timer("You duck into the locker room. It's empty, but you spot something on the bench.")
        print_timer("A potion! You read the label.")
        print_timer("It'll increase your stamina! You down it and feel envigorated.\n(Your health points increase by 25)")
        print_timer("You return to the arena entrance.")
        # add message if you already have potion
    if choice == "2":
        print_timer("You step out into the sand to the roaring crowd, the sun high above.")
        opponent = random.choice(opponents)
        print_timer("The announcer shouts your name, and then another: " + opponent + ".")
        print_timer("You see them across the sand, brandishing their weapon.")
        print_timer("Before stepping further into the arena, you turn to the weapon rack."
                    "You have your pick of the lot.\n"
                    "Enter 1 for a large axe.\n"
                    "Enter 2 for a shortsword.\n"
                    "Enter 3 for a greatsword.\n")
        weapon = input("Select your weapon: (Please enter 1, 2, or 3)\n")
        if weapon == "1":
            print_timer("You select the large axe. It feels good in your hand.\n You step up to your opponent.")
        if weapon == "2":
            print_timer("You select the shortsword. It feels good in your hand.\n You step up to your opponent.")
        if weapon == "3":
            print_timer("You select the greatsword. It feels good in your hand.\n You step up to your opponent.")
