from random import randint
from art import logo

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
        statement = True
        while statement:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.")
                print("Guess again.")
            elif guess < number:
                print("Too low.")
                print("Guess again.")
            else:
                print(f"You got it! The answer was {number}.")
                statement = False
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                statement = False
    elif difficulty == "hard":
        attempts = 5
        statement = True
        while statement:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.")
                print("Guess again.")
            elif guess < number:
                print("Too low.")
                print("Guess again.")
            else:
                print(f"You got it! The answer was {number}.")
                statement = False
            attempts -= 1
            # print(f"You have {attempts} attempts remaining to guess the number.")
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                statement = False
            
    else:
        print("Invalid difficulty. You lose!")
        return

guess_the_number()