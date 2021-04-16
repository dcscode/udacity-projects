# elevator game

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
        result = "win"
        print_timer("You win!")
        tickets += 5
        print_timer("The machine spits out 5 tickets.")
        print_timer("You have " + str(tickets) + " tickets.")
    elif "sportsball" in game:
        print_timer("You play Sportsball")
        player = random.randint(1,10)
        sportsball = random.randint(1,10)
        if player > sportsball:
            print_timer("You: " + str(player))
            print_timer("Sportsball: " + str(sportsball))
            print_timer("You win!")
            tickets += 20
        elif player < sportsball:
            print_timer("You: " + str(player))
            print_timer("Sportsball: " + str(sportsball))
            print_timer("You lose!")
        else:
            print_timer("You: " + str(player))
            print_timer("Sportsball: " + str(sportsball))
            print_timer("You tie!")
            tickets += 10
        print_timer("You have " + str(tickets) + " tickets.")
    
