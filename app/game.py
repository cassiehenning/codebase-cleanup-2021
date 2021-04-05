
import os 
from random import choice


#
# USER SELECTION
#

VALID_OPTIONS = ["rock", "paper", "scissors"]

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