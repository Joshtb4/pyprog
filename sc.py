import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors: ")

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()
