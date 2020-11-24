import random


class Game:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.options = input()
        if self.options == "":
            self.options = ["scissors", "paper", "rock"]
        else:
            self.options = self.options.split(",")
            self.options = self.options[::-1]
        print("Okay, let's start")
        self.scores = self.get_scores()
        self.score = self.init_score()

    def get_scores(self):
        try:
            rate = open("rating.txt", "r")
            lines = rate.readlines()
            rate.close()
            return lines

        except FileNotFoundError:
            return []

    def init_score(self):
        for line in self.scores:
            if line.startswith(self.name):
                score = line.split()
                self.scores.remove(line)
                return int(score[1])
        else:
            return 0

    def winner(self, player, ai):  # decides, who won
        player_ind = self.options.index(player)
        relation = self.options[player_ind + 1:] + self.options[:player_ind]
        relation = relation[:len(relation) // 2]

        if ai in relation:
            return "player"
        else:
            return "ai"

    def play(self, player):  # prints message to user,
        ai = random.choice(self.options)
        if player == ai:
            print("There is a draw ({})".format(ai))
            self.score += 50
            return 0
        if self.winner(player, ai) == "player":
            print("Well done. The computer chose {} and failed".format(ai))
            self.score += 100
        else:
            print("Sorry, but the computer chose {}".format(ai))

    def print_score(self):
        print("Your rating:", self.score)

    def exit(self):
        rate = open("rating.txt", "w")
        if self.scores:
            for line in self.scores:
                rate.write(line)
        rate.write(str(self.name) + " " + str(self.score) + "\n")
        rate.close()

    def menu(self):
        inp = input()
        for j in self.options:
            if j == inp:
                self.play(inp)
                break
        else:
            if inp == "!rating":
                self.print_score()
            elif inp == "!exit":
                self.exit()
                return 0
            else:
                print("Invalid input")

        return 1

my_game = Game()

while my_game.menu():
    pass
