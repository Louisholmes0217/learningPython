# First project to build a small rock paper scissors game
import random

# Defining recursive "keep playing" alg to easily loop until we get a valid result
def keep_playing():
    choice = input("Would you like to play again? y/n:    ")
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        print("please enter a valid option")
        keep_playing()    


# Defining options, player score, computer score and introducing the game
options = ["rock", "paper", "scissors"]
comp_score = 0
player_score = 0
print("Welcome to rock paper scissors!")

keep_going = True
while keep_going:
    player_choice = input("Please enter rock, paper, or scissors\n: ")  # getting user input
    computer_choice = options[random.randint(0,2)]                      # computer making choice 

    if player_choice == "rock":         # series of comparing choices
        if computer_choice == "rock":
            print("you draw!")
            comp_score += 1
            player_score += 1

        elif computer_choice == "paper":
            print("you lose!")
            comp_score += 1

        elif computer_choice == "scissors":
            print("you win!")
            player_score += 1

    if player_choice == "paper":
        if computer_choice == "rock":
            print("you win!")
            player_score += 1

        elif computer_choice == "paper":
            print("you draw!")
            comp_score += 1
            player_score += 1

        elif computer_choice == "scissors":
            print("you lose!")
            comp_score += 1 

    if player_choice == "scissors":
        if computer_choice == "rock":
            print("you lose!")
            comp_score += 1

        elif computer_choice == "paper":
            print("you win!")
 
            player_score += 1

        elif computer_choice == "scissors":
            print("you draw!")
            comp_score += 1 
            player_score += 1
    else:
        print("invalid option")
    
    print("Current score = computer: {}, player: {}".format(comp_score, player_score))
    keep_going = keep_playing()

print("Thanks for playing!\nFinal score is Computer: {}, Player: {}".format(comp_score, player_score))

