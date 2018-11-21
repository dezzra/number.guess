# template for "Guess the number" mini-project

import simplegui
import random

range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global count
    global secret_number
    global range
    if (range == 100):
        secret_number = random.randrange(0, 100)
        count = 7
        print("Guess the number from 0 to 99!")
        return
    elif (range == 1000):
        secret_number = random.randrange(0, 1000)
        count = 10
        print("Guess the number from 0 to 999!")
        return
    return

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global range
    range = 100
    new_game()
    return

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global range
    range = 1000
    new_game()
    return
    
def input_guess(guess):
    global count
    count = count - 1
    
    if (int(guess) > secret_number) and (count > 1):
        print("Your guess was " + str(guess) + ".")
        print("Lower! You have " + str(count) + " guesses left.")
        return
    elif (int(guess) < secret_number) and (count > 1):
        print("Your guess was " + str(guess) + ".")
        print("Higher! You have " + str(count) + " guesses left.")
        return
    if (int(guess) > secret_number) and (count == 1):
        print("Your guess was " + str(guess) + ".")
        print("Lower! You have " + str(count) + " guess left.")
        return
    elif (int(guess) < secret_number) and (count == 1):
        print("Your guess was " + str(guess) + ".")
        print("Higher! You have " + str(count) + " guess left.")
        return
    elif (int(guess) == secret_number) and (count >= 0):
        print("Congratulations, " + str(secret_number) + " is correct! You win!")
        print("")
        new_game()
        return
    elif count == 0:
        print("Your guess was " + str(guess) + ".")
        print("Too bad! Out of guesses. The number was " + str(secret_number) + ".")
        print("")
        new_game()

# create frame
frame = simplegui.create_frame("Guess the Number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Guess:", input_guess, 50)
frame.add_button("New Game", new_game)
frame.add_button("Set Range: 100", range100)
frame.add_button("Set Range: 1000", range1000)

frame.start

# call new_game
new_game()
