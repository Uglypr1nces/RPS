import random
from game.round import *
from game.utils import *

choices = [ROCK, PAPER, SCISSOR]


class Game:
    def __init__(self):
        self.rounds_played = 0

    def play(self):
        while True:
            player_choice = input("What do you want to pick? (Rock, Paper, or Scissors): ").lower()
            if player_choice in choices:
                computer_choice = random.choice(choices)
                print(f"Player picked {player_choice.capitalize()}, Computer picked {computer_choice.capitalize()}")
                game_round = Round(player_choice, computer_choice)
                self.rounds_played += 1
                outcome = game_round.evaluate()
                print(outcome.to_string())
                print(f"Rounds played: {self.rounds_played}")
            else:
                print("Please pick one of the options listed.")
