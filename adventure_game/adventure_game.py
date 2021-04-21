import time
import random
 
player_health = 25
opponent_health = 25
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
        print_timer("It'll increase your stamina! You down it and feel envigorated.\n(Your health points increase by 10)")
        player_health += 15
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
        print_timer("Weapon in hand, it's time to fight.")
        attack_first = input("Do you attack first? (Please enter y/n)\n").lower()
        if attack_first == "y":
            print_timer("You lunge and swing your weapon!")
            player_damage = random.randint(5, 25)
            print_timer("You deal " + str(player_damage) + " damage.")
            if player_damage > opponent_health:
                print_timer("You defeated them!")
                break
            opponent_health -= player_damage
            print_timer(opponent + " health: " + str(opponent_health))
        if attack_first == "n":
            print_timer("You wait as you and your opponent circle each other.")
            print_timer("They lunge!")
            opponent_damage = random.randint(5, 25)
            print_timer("They deal" + str(opponent_damage) + " damage.")
            if opponent_damage > player_health:
                print_timer("You are defeated.")
                break
            player_health -= opponent_damage
            print_timer("Your health: " + str(player_health))
        while player_health > 0:
            opponent_damage = random.randint(5, 25)
            print_timer("Your opponent deals " + str(opponent_damage) + ".")
            if opponent_damage > player_health:
                print_timer("You are defeated.")
                break
            player_health -= opponent_damage
            print_timer("Your health: " + str(player_health))
            player_damage = random.randint(5, 25)
            print_timer("You deal " + str(player_damage) + ".")
            if player_damage > opponent_health:
                print_timer("You defeated them!")
                break
            opponent_health -= player_damage
            print_timer(opponent + " health: " + str(opponent_health))
            
            
