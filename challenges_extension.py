import random

correct_answer = random.randint(1, 100)

while True:
    user_input = int(input("Guess a number between 1 and 100: "))

    if user_input < correct_answer:
        print("Too Low")
    elif user_input >  correct_answer:
        print("Too high")
    else:
    
        print("congragulations!")
    
        
        




    
    

                     