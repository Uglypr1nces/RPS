from game.utils import *

class Outcome:
    # winner is a string or None if it's a tie
    def __init__(self, winner):
        self.winner = winner

    def to_string(self):
        if self.winner:
            return f"{self.winner} won!"
        return "It's a tie!"

class Round:

    def __init__(self, player_choice, computer_choice):
        self.player_choice = player_choice
        self.computer_choice = computer_choice

    def evaluate(self) -> Outcome:
        outcome: Outcome = self.get_result()
        return outcome

    def get_result(self):
        if self.player_choice == self.computer_choice:
            return Outcome(winner=None)
        elif (self.player_choice == ROCK and self.computer_choice == SCISSOR) or \
             (self.player_choice == PAPER and self.computer_choice == ROCK) or \
             (self.player_choice == SCISSOR and self.computer_choice == PAPER):
            return Outcome("Player")
        else:
            return Outcome("Computer")
