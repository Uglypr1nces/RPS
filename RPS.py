import random

def winner_checker(choice1,choice2):
    if choice1 == "rock" and choice2 == "scissors" or choice1 == "paper" and choice2 == "rock" or choice1 == "scissors" and choice2 == "paper":
        print(f"player won, player picked {choice1}, computer picked {choice2}")
    elif choice2 == "rock" and choice1 == "scissors" or choice2 == "paper" and choice1 == "rock" or choice2 == "scissors" and choice1 == "paper":
        print(f"copmuter won, player picked {choice1}, computer picked {choice2}")
    else:
        print("tie")

while True:
    choice = input("What do you want to pick? (Rock, Paper or scissors)")
    choices = ["rock", "paper","scissors"]

    if choice in choices:
        computerchoice = random.choice(choices)
        winner_checker(choice,computerchoice)

    else:
        print("please pick one of the options listed")