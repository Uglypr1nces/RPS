import random
from game.round import *
from game.utils import *
import sys
import time

class Game:
    def __init__(self):
        self.rounds_played = 0
        self.player_wins = 0
        self.computer_wins = 0

    def waiting_animation(self,wait_time):
        while wait_time != 0:
            sys.stdout.write('\rloading |')
            time.sleep(0.1)
            sys.stdout.write('\rloading /')
            time.sleep(0.1)
            sys.stdout.write('\rloading -')
            time.sleep(0.1)
            sys.stdout.write('\rloading \\')
            time.sleep(0.1)
            wait_time -= 1
        sys.stdout.write('\rDone!     ')

    def play(self):
        while True:
            player_choice = input("What do you want to pick? (Rock, Paper, or Scissors): ").lower()
            if player_choice in choices:
                computer_choice = random.choice(choices)
                self.waiting_animation(5)
                print(f"Player picked {player_choice.capitalize()}, Computer picked {computer_choice.capitalize()}")
                game_round = Round(player_choice, computer_choice)
                outcome = game_round.evaluate()
                self.waiting_animation(3)
                print(outcome.to_string())

                if "Player" in outcome.to_string():
                    self.player_wins += 1
                elif "Computer" in outcome.to_string():
                    self.computer_wins += 1

                self.rounds_played += 1
                self.waiting_animation(3)
                print(f"Rounds played: {self.rounds_played}. Player wins: {self.player_wins}, Computer wins: {self.computer_wins}")
            else:
                print("Please pick one of the options listed.")
