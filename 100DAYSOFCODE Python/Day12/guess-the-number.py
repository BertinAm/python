# Day12 100DaysOfCodePython
# Guess the Number Game
# making use of the randint method from the random module
from random import randint
# importing the logo from the art module
from art import logo
# creating a function called guess_the_number
def guess_the_number():
    # printing the logo
    print(logo)
    # printing a welcome message
    print("Welcome to the Number Guessing Game!")
    # printing a message to the user
    print("I'm thinking of a number between 1 and 100.")
    # creating a variable called number to store a random number between 1 and 100
    number = randint(1, 100)
    # creating a variable called difficulty to store the users difficulty choice
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # creating an if statement to check if the user chose easy
    if difficulty == "easy":
        # creating a variable called attempts to store the number of attempts the user has
        attempts = 10
        # creating a variable called statement to store the boolean value
        statement = True
        # creating a while loop to ask the user to make a guess
        while statement:
            # printing a message to the user
            print(f"You have {attempts} attempts remaining to guess the number.")
            # asking the user to make a guess
            guess = int(input("Make a guess: "))
            # creating an if statement to check if the users guess is greater than the number
            if guess > number:
                # printing a message to the user
                print("Too high.")
                print("Guess again.")
            # creating an elif statement to check if the users guess is less than the number
            elif guess < number:
                # printing a message to the user
                print("Too low.")
                print("Guess again.")
            # creating an else statement to check if the users guess is equal to the number
            else:
                # printing a message to the user
                print(f"You got it! The answer was {number}.")
                # changing the value of the statement variable to False
                statement = False
            # subtracting 1 from the attempts variable
            attempts -= 1
            # creating an if statement to check if the attempts variable is equal to 0
            if attempts == 0:
                # printing a message to the user
                print("You've run out of guesses, you lose.")
                # changing the value of the statement variable to False
                statement = False
    # creating an elif statement to check if the user chose hard
    elif difficulty == "hard":
        # creating a variable called attempts to store the number of attempts the user has
        attempts = 5
        # creating a variable called statement to store the boolean value
        statement = True
        # creating a while loop to ask the user to make a guess
        while statement:
            # printing a message to the user
            print(f"You have {attempts} attempts remaining to guess the number.")
            # asking the user to make a guess
            guess = int(input("Make a guess: "))
            # creating an if statement to check if the users guess is greater than the number
            if guess > number:
                # printing a message to the user
                print("Too high.")
                print("Guess again.")
            # creating an elif statement to check if the users guess is less than the number
            elif guess < number:
                # printing a message to the user
                print("Too low.")
                print("Guess again.")
            # creating an else statement to check if the users guess is equal to the number
            else:
                # printing a message to the user
                print(f"You got it! The answer was {number}.")
                # changing the value of the statement variable to False
                statement = False
            # subtracting 1 from the attempts variable
            attempts -= 1
            # creating an if statement to check if the attempts variable is equal to 0
            if attempts == 0:
                # printing a message to the user
                print("You've run out of guesses, you lose.")
                # changing the value of the statement variable to False
                statement = False
    
    # creating an else statement to check if the user chose an invalid difficulty
    else:
        # printing a message to the user
        print("Invalid difficulty. You lose!")
        statement = False

# calling the guess_the_number function
guess_the_number()