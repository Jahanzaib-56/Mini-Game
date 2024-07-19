# ROCK - PAPER - SCISSOR Game

# Using RANDOM and TIME Modules
import random
import time

print("ROCK _ PAPER _ SCISSOR")

time.sleep(1)

print("Best of 3")

time.sleep(1)

# Initial game state
computer_won = 0
you_won = 0
games_tied = 0

# Using for-loop to repeat the process for 3 times making it a 3 rounds game
for _ in range(3):

    # Prompitng user choice
    My_choice = input("Enter your Choice, Rock, Paper or Scissor: ")

    # Delaying the computer response by 1 seconds
    time.sleep(1)

    # Declaring choices for computer to select.
    choices = ["Rock", "Paper", "Scissor"]

    # Taking Computer Choice.
    Computer_Choice = random.choice(choices)
    print(f"Computer chose: {Computer_Choice}")

    # Delaying final desicion by 1 seconds
    time.sleep(1)

    # Using Conitionals to decide WINNER and LOSER
    if (My_choice == Computer_Choice):
        result = "TIED!"
        print(result)
    elif (My_choice == "Rock" and Computer_Choice == "Scissor"):
        result = "YOU WIN!"
        print(result)
    elif (My_choice == "Rock" and Computer_Choice == "Paper"):
        result = "COMPUTER WINS!"
        print(result)
    elif (My_choice == "Paper" and Computer_Choice == "Scissor"):
        result = "COMPUTER WINS!"
        print(result)
    elif (My_choice == "Paper" and Computer_Choice == "Rock"):
        result = "YOU WIN!"
        print(result)
    elif (My_choice == "Scissor" and Computer_Choice == "Rock"):
        result = "COMPUTER WINS!"
        print(result)
    elif (My_choice == "Scissor" and Computer_Choice == "Paper"):
        result = "YOU WIN!"
        print(result)
    else:
        print("Please enter valid choice with first letter Capital.")        

    # Evaluating final game state
    if (result == "COMPUTER WINS!"):
        computer_won += 1
    elif (result == "YOU WIN!"):
        you_won += 1
    elif (result == "TIED!"):
        games_tied += 1    

print("Evaluating Final Result")

# Delaying final result by 1 second
time.sleep(1)

# Game Conclusion
print(f"You Won: {you_won} Games")                                        
print(f"Computer Won: {computer_won} Games")
print(f"Games tied: {games_tied}") 