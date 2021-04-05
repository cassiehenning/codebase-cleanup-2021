

from app.game import determine_winner

def test_determine_winner(): 
    determine_winner("rock", "rock") == None 
    determine_winner("rock", "paper") == "paper"
    determine_winner("rock", "scissors") == "rock"

    determine_winner("paper", "rock") == "paper"
    determine_winner("paper", "paper") == None 
    determine_winner("paper", "scissors") == "scissors" 

    determine_winner("scissors", "rock") == "rock"
    determine_winner("scissors", "paper") == "scissors"
    determine_winner("scissors", "scissors") == None 





















