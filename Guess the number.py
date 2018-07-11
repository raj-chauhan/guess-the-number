# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game():
    print ("-This is a new game")
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,100,1)
    global remaining_guesses
    remaining_guesses = 7
    print ("You have", remaining_guesses, "guesses left.")
    
# define event handlers for control panel
def range100():
    print ("-This is a new game")
    global secret_number
    # button that changes the range to [0,100) and starts a new game 
    secret_number = random.randrange(0,100)
    print ("The range is now [0,100)")
    global remaining_guesses
    remaining_guesses = 7
    print ("You have", remaining_guesses, "guesses left.")
    
def range1000():
    print ("-This is a new game"
    global secret_number
    # button that changes the range to [0,1000) and starts a new game     
    secret_number = random.randrange(0,1000)
    print ("The range is now [0,1000)")
    #print secret_number
    global remaining_guesses
    remaining_guesses = 10
    print ("You have", remaining_guesses, "guesses left.")
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    print ("--Guess was", guess)
    
    global remaining_guesses
    remaining_guesses = remaining_guesses - 1
    
    if guess == secret_number:
        print ("Correct !!!")
        print (" ")
        new_game()
    elif remaining_guesses == 0:
        print ("you have", remaining_guesses, "guesses left.")
        print ("The number was", secret_number)
        print (" ")
        new_game()
    elif guess < secret_number:
        print ("HINT: Higher")
        print ("you have", remaining_guesses, "guesses left.")
    elif guess > secret_number:
        print ("HINT: Lower")
        print ("you have", remaining_guesses, )
    else:
        "incorrect selection"

# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_input("Enter the guess",input_guess,150)
frame.add_button("Range is [0,100)",range100,150)
frame.add_button("Range is [0,1000)",range1000,150)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
