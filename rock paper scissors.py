import random

playcount = 0
playagain_count = 0

while playcount == 0:
    rngai = ["Rock", "Paper", "Scissors"]
    "Rock" > "Scissors"
    "Paper" > "Rock"
    "Scissors" > "Paper"

    aichoice = random.choice(rngai)

    player_input = input("Rock, Paper, or Scissors? ")

    if str(aichoice) < str(player_input):
        print("The AI chose " + aichoice + ", You Lose!")
    if str(aichoice) > str(player_input):
        print("The AI chose " + aichoice + ", You Win!")
    if str(aichoice) == str(player_input):
        print("The AI chose " + aichoice + ", Its a tie!")

    
    play_again = input("Do you want to play again (y or n)? ")
    if play_again == "n":
        playcount += 1
    playagain_count += 1
    if play_again == "y":
        playcount += 0
    else:
        print("Invalid Input!")
    

    
