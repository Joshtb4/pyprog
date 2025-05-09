

# def rock_paper_scissors_lizard_spock(player1, player2):
#     
#     player1 = player1.lower()
#     player2 = player2.lower()

  
#     moves = ["rock", "paper", "scissors", "lizard", "spock"]

   
#     if player1 not in moves or player2 not in moves:
#         return "Invalid"

    
#     if player1 == player2:
#         return "Tie game"

  
#     if player1 == "rock":
#         if player2 == "scissors" or player2 == "lizard":
#             return "Player 1 wins!"
#         else:
#             return "Player 2 wins!"
    
#     elif player1 == "paper":
#         if player2 == "rock" or player2 == "spock":
#             return "Player 1 wins!"
#         else:
#             return "Player 2 wins!"
    
#     elif player1 == "scissors":
#         if player2 == "paper" or player2 == "lizard":
#             return "Player 1 wins!"
#         else:
#             return "Player 2 wins!"

#     elif player1 == "lizard":
#         if player2 == "spock" or player2 == "paper":
#             return "Player 1 wins!"
#         else:
#             return "Player 2 wins!"

#     elif player1 == "spock":
#         if player2 == "scissors" or player2 == "rock":
#             return "Player 1 wins!"
#         else:
#             return "Player 2 wins!"

# print(rock_paper_scissors_lizard_spock("lizard", "spock")) 



def rock_paper_scissors_game(player_1, player_2):
   
    winning_combinations = {
        "rock": ["scissors", "lizard"], 
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    player_1 = player_1.lower()
    player_2 = player_2.lower() 

    if player_1 not in winning_combinations or player_2 not in winning_combinations:
        return "not correct input"
    if player_1 == player_2:
        return "player 1 and player 2 draw"
    elif player_2 in winning_combinations[player_1]:
        return "player 1 wins"
    else:
        return "player 2 wins"
    

print(rock_paper_scissors_game("rock", "paper"))



