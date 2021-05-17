import random
moves = ['rock', 'paper', 'scissors']

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
        while True:
            move = input("rock, paper, scissors? > ").lower()
            if move in moves:
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
        elif self.my_move is moves[1]:
            self.my_move = moves[2]
        elif self.my_move is moves[2]:
            self.my_move = moves[0]
        return self.my_move

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
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
            if self.p1.score >= 3 or self.p2.score >= 3:
                break
        print("Game over!")
        print("Best 3 of 5")
        if self.p1.score > self.p2.score:
            print("Player One wins!")
            print(f"Score: Player One {self.p1.score} "
                  f"Player Two {self.p2.score}")
        if self.p1.score < self.p2.score:
            print("Player Two wins!")
            print(f"Score: Player One {self.p1.score} "
                  f"PLayer Two {self.p2.score}")
        if self.p1.score == self.p2.score:
            print("Tie!")
            print(f"Score: Player One {self.p1.score} "
                  f"PLayer Two {self.p2.score}")

players = (Player(), ReflectPlayer(), RandomPlayer(),     CyclePlayer())

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(players))
    game.play_game()
