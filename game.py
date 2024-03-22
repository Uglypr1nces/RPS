import random
from round import Round

class Game:
    choices = ["rock","paper","scissors"]

    def play(self):
        while True:
            player_choice = input("what do you want to pick? (Rock, Paper or Scissors): ")
            if player_choice.lower() in self.choices:
                computer_choice = random.choice(self.choices)
                round = Round(player_choice, computer_choice)
                round.evaluate()
            else:
                print("Please pick one of the options listed.")


game = Game()
game.play()