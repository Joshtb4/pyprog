import random


def high_low():
     rand = random.randint(1,100)
     playing = True
     while playing:
        try:
            guess = int(input("Guess a number between 1 and 100: "))  
            if guess == rand:
                print("Congrats! You guessed it!")
                playing = False
            else:
                print("LOWER" if guess > rand else "HIGHER")
        except ValueError:
            print("Invalid input! Please enter an integer.")  

play = "y"
while play == "y":
    high_low()
    play = input("play again? (y/n)")

print("game over!")
