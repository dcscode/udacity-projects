import random
moves = ['rock', 'paper', 'scissors']

#The Player class is the parent class for
#all of the Players in this game


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None
        
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
            
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        move = input("rock, paper, scissors? > ").lower()
        return move
        
class ReflectPlayer(Player):
    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
        return self.my_move
    
    def learn(self, my_move, their_move):
        self.my_move = their_move

class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
        elif self.my_move is moves[0]:
            self.my_move = moves[1]
        elif self
        
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))
            
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if self.beats(move1, move2):
            print("Player One Wins!")
            self.p1.score += 1
        elif self.beats(move2, move1):
            print("Player Two Wins!")
            self.p2.score += 1
        else:
            print("Tie!")
        print(f"Score: Player One {self.p1.score}, PLayer Two {self.p2.score}")
        
        
    def play_game(self):
        self.p1.score = 0
        self.p2.score = 0
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
