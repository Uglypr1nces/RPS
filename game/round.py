class Round:
    RESULT_MESSAGES = {
    "win": "Player won!",
    "lose": "Computer won!",
    "tie": "It's a tie!"
    }

    def __init__(self, player_choice, computer_choice):
        self.player_choice = player_choice
        self.computer_choice = computer_choice

    def evaluate(self):
        result = self.get_result()
        print(f"Player picked {self.player_choice.capitalize()}, Computer picked {self.computer_choice.capitalize()}. {self.RESULT_MESSAGES[result]}")

    def get_result(self):
        if self.player_choice == self.computer_choice:
            return "tie"
        elif (self.player_choice == "rock" and self.computer_choice == "scissors") or \
             (self.player_choice == "paper" and self.computer_choice == "rock") or \
             (self.player_choice == "scissors" and self.computer_choice == "paper"):
            return "win"
        else:
            return "lose"