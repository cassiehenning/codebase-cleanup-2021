
import os 
from random import choice


#
# USER SELECTION
#

VALID_OPTIONS = ["rock", "paper", "scissors"]

<<<<<<< HEAD
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock": 
    if c == "rock": 
        print("You tied!")
    elif c == "paper":
        print("The computer won!")
    elif c == "scissors":
        print("You won!")
elif u == "paper": 
    if c == "rock": 
        print("You won!")
    elif c == "paper":
        print("You tied!")
    elif c == "scissors":
        print("The computer won!")
elif u == "scissors": 
    if c == "rock": 
        print("The computer won!")
    elif c == "paper":
        print("You won!")
    elif c == "scissors":
        print("You tied!")

#there are even less complex ways of doing this 
#using a single dictionary
#touple approace 
=======
def determine_winner(choice1, choice2):
    """
    Choice 1 and Choice 2 are both string : one of "rock", "paper", or "scissors"
    """
    winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice
    


if __name__ == '__main__': 

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(u,c)

    if winner == u: 
        print("YOU WON!")
    elif winner == c: 
        print("COMPUTER WON!")
    elif winner == None: 
        print("TIE")
>>>>>>> simple
