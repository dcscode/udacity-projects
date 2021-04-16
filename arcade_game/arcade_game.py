# arcade game

import time

import random

results = ["win","lose"]
tickets = 0

def print_timer(string):
    print(string)
    time.sleep(2)
    
print_timer("You are at the arcade.\n"
            "There are three games you want to play.\n"
            "Robots vs Tigers\n"
            "Neon Dance\n"
            "Sportsball\n")

while True:
    game = input("What game do you want to play?\n").lower()
    if "robots vs tigers" in game:
        print_timer("You play Robots vs Tigers.")
        result = random.choice(results)
        print_timer("You " + result + "!")
        if result == "win":
            tickets += 10
            print_timer("The machine spits out 10 tickets.")
        print_timer("You have " + str(tickets) + " tickets.")
    elif "neon dance" in game:
        print_timer("You play Neon Dance.")
    elif "sportsball" in game:
        print_timer("You play Sportsball")
