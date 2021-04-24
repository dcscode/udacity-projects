import time
import random

player_health = 25
opponent_health = 25
inventory = []
opponents = ["opponent 1", "opponent 2", "opponent 3", "opponent 4"]


def print_timer(string):
    print(string)
    time.sleep(1)


def intro():
    print_timer("You seek glory.")
    print_timer("You have come to the arena to claim it.")


def weapon():
    while True:
        weapon = input("Select your weapon: (Please enter 1, 2, or 3)\n")
        if weapon == "1":
            print_timer("You select the large axe. It feels good in your hand.\n"
                    "You step up to your opponent.")
            break
        if weapon == "2":
            print_timer("You select the shortsword. It feels good in your hand.\n"
                    "You step up to your opponent.")
            break
        if weapon == "3":
            print_timer("You select the greatsword. It feels good in your hand.\n"
                    "You step up to your opponent.")
            break


def fight():
    opponent = random.choice(opponents)
    print_timer("The announcer shouts your name,"
                " and then another: " + opponent + ".")
    opponent_health = 25
    if "potion" in inventory:
        player_health = 35
    else:
        player_health = 25
    while True:
        attack_first = input("Do you attack first? (Please enter y/n)\n").lower()
        if attack_first == "y":
            print_timer("You lunge and swing your weapon!")
            player_damage = random.randint(5, 25)
            print_timer("You deal " + str(player_damage) + " damage.")
            if player_damage > opponent_health:
                print_timer("You defeated them! You're the champion!"
                            " Glory forever!")
            opponent_health -= player_damage
            print_timer(opponent + " health: " + str(opponent_health))
            break
        elif attack_first == "n":
            print_timer("You wait as you and your opponent circle each other.")
            print_timer("They lunge!")
            opponent_damage = random.randint(5, 25)
            print_timer("They deal " + str(opponent_damage) + " damage.")
            if opponent_damage > player_health:
                print_timer("You are defeated.")
            elif player_health == 0:
                print_timer("You are defeated.")
                result = "loss"
            player_health -= opponent_damage
            print_timer("Your health: " + str(player_health))
            break
    while player_health > 0:
        opponent_damage = random.randint(5, 25)
        print_timer("Your opponent deals " + str(opponent_damage) + " damage.")
        if opponent_damage > player_health:
            print_timer("You are defeated.")
            break
        player_health -= opponent_damage
        print_timer("Your health: " + str(player_health))
        player_damage = random.randint(5, 25)
        if player_health == 0:
            print_timer("You are defeated.")
            break
        print_timer("You deal " + str(player_damage) + " damage.")
        if player_damage > opponent_health:
            print_timer("You defeated them! You're the champion!"
                        " Glory forever!")
            break
        opponent_health -= player_damage
        if opponent_health == 0:
            print_timer("You defeated them! You're the champion!"
                        " Glory forever!")
            break
        print_timer(opponent + " health: " + str(opponent_health))


def room():
    while True:
        choice = input("Enter 1 to visit the locker room.\n"
                       "Enter 2 to step onto the field.\n"
                       "Which will you choose? (Please enter 1 or 2)\n")
        if choice == "1":
            if "potion" in inventory:
                print_timer("Just an empty locker room.")
            else:
                inventory.append("potion")
                print_timer("You duck into the locker room."
                            " It's empty but you spot something on the bench.")
                print_timer("A potion! You read the label.")
                print_timer("It'll increase your stamina! "
                            "You down it and feel envigorated.\n"
                            "(Your health points increase by 10)")
                print_timer("Your health: 35")
            print_timer("You return to the arena entrance.")
        if choice == "2":
            print_timer("You step out into the sand to the"
                        "roaring crowd, the sun high above.")
            print_timer("Before stepping further into the arena,"
                        " you turn to the weapon rack."
                        " You have your pick of the lot.\n"
                        "Enter 1 for a large axe.\n"
                        "Enter 2 for a shortsword.\n"
                        "Enter 3 for a greatsword.\n")
            weapon()
            fight()
            if "potion" in inventory:
                inventory.remove("potion")
            new_game()


def new_game():
    new_game = input("Would you like to play again?"
                     " Please enter 'again' to play again"
                     " or 'no' to quit.\n").lower()
    if new_game == "again":
        print_timer("Good luck!")
        intro()
        room()
    if new_game == "no":
        print_timer("Thanks for playing!")
        exit()


def arena_game():
    intro()
    room()

arena_game()
