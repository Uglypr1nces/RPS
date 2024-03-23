class Round:

    RESULT_MESSAGES = {
    "win": "Player won!",
    "lose": "Computer won!",
    "tie": "It's a tie!"
    }

    def __init__(self, player_choice, computer_choice):
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        self.player_wins = 0
        self.computer_wins = 0
        self.rounds_played = 0

    def evaluate(self):
        result = self.get_result()

        print(f"Player picked {self.player_choice.capitalize()}, Computer picked {self.computer_choice.capitalize()}. {self.RESULT_MESSAGES[result]}")
        print(f"player wins: {self.player_wins}, computer wins: {self.computer_wins}, total rounds played: {self.rounds_played}")

    def get_result(self):
        if self.player_choice == self.computer_choice:
            self.rounds_played += 1
            return "tie"
        elif (self.player_choice == "rock" and self.computer_choice == "scissors") or \
             (self.player_choice == "paper" and self.computer_choice == "rock") or \
             (self.player_choice == "scissors" and self.computer_choice == "paper"):
            self.player_wins += 1
            self.rounds_played += 1
            return "win"
        else:
            self.computer_wins += 1
            self.rounds_played += 1
            return "lose"
