import random
from round import Round

class Game:
    choices = ["rock", "paper", "scissors"]

    def __init__(self):
        self.rounds_played = 0

    def play(self):
        while True:
            player_choice = input("What do you want to pick? (Rock, Paper, or Scissors): ").lower()
            if player_choice in self.choices:
                computer_choice = random.choice(self.choices)
                game_round = Round(player_choice, computer_choice)
                self.rounds_played += 1
                game_round.evaluate()
                print(f"Rounds played: {self.rounds_played}")
            else:
                print("Please pick one of the options listed.")

game = Game()
game.play()
