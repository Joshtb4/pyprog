'''The function takes two integer parameters and returns a string that says who won which should be either “player1” or “player2”. The winner depends on the rolls being odd or even as follows: 
If player 1 rolls an even, player 2 must roll an odd, and vice versa.  
Hence, both numbers being odd or both numbers being even means player 1 wins, 
one odd and one even means player 2 wins.  
Test your program with a reasonable set of combinations of dice roll. 
'''




def checker(p1, p2):
    if p1 % 2 == p2 % 2:
        return "player1"
    else:
        return "player2"
    

print(checker(15, 56))




