"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


# Here the main loop for the game is put into a function, that way it can be used more than once within the start game function

def game_loop():
    # get a random number between 1 and 10
    rand = random.randint(1, 10)
    tries = 1
    high_scores = []
    # ask the user to guess until they guess the right answer, 
    # here the loop is wrapped in a try-except block in case the user enters an invalid value
    while True:
        try:
            guess = int(input("Guess the number: (1-10)  "))
            if guess > 10:
                print("The Value you entered is out of range")
            elif guess > rand:
                print("Go Lower")
                tries += 1
            elif guess < rand:
                print("Go Higher")
                tries += 1
            elif guess == rand:
                print("\nCongratulations you guessed the correct number in " + str(tries) + " tries")
                print()
                # This code adds the first value to the high scores list and if a value is lower than 
                # the lowest value it is then added and the final value of the list is printed out
                if len(high_scores) == 0:
                    high_scores.append(tries)
                elif min(high_scores) > tries:
                    high_scores = tries
                print("The high score is: " + str(high_scores[-1]))
                break
        except ValueError:
            print("Please enter a valid value")


def start_game():
    print("=============================")
    print("Welcome to the guessing game")
    print("============================")

    game_loop()
    # the game loop is called and then there is a while loop that replays the game until the user exits
    while True:
        play_again = input("Would you like to play again? (Y/N) ")
        if play_again.capitalize() == "Y":
            game_loop()
        elif play_again.capitalize() == "N":
            print("\nThanks For Playing!!!")
            break
        else:
            print("You entered an invalid value")



# Kick off the program by calling the start_game function.
start_game()