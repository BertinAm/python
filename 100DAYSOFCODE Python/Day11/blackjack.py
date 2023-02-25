# making use of the choice method from the random module
from random import choice
# making use of the sample method from the random module
from random import sample
# making use of the system method from the os module
from os import system
# importing the logo from the art module
from art import logo
# creating a function called deal_card
def deal_card():
    # creating a variable called users_choice to store the boolean value
    users_choice = True
    # creating a while loop to ask the user if they want to play a game of blackjack
    while users_choice:
            # creating a list containing numbers that corresponds to cards
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            # creating an empty list called users_cards
            user_cards = []
            # selecting 2 random numbers from the cards list
            user_cards = sample(cards, 2)
            # creating an empty list called computer_cards
            computer_cards = []
            # selecting a random number from the cards list
            computer_cards = choice(cards)
            # printing the users cards and the sum of the users cards
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            # printing the computers first card
            print(f"Computer's first card: {computer_cards}")
            # creating a variable called statement to store the boolean value
            statement = True
            # creating a while loop to ask the user if they want to get another card or pass
            while statement:
                # asking the user if they want to get another card or pass
                response = input("Type 'y' to get another card,, type 'n' to pass: ")
                # creating an if statement to check if the user wants to get another card
                if response == 'y':
                    # selecting a random number from the cards list
                    user_cards.append(choice(cards))
                    # printing the users cards and the sum of the users cards
                    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                    # printing the computers first card
                    print(f"Computer's first card: {computer_cards}")
                    # creating an if statement to check if the sum of the users cards is greater than 21
                    if sum(user_cards) > 21:
                        # printing a message to the user
                        print("You went over. You lose")
                        # changing the value of the statement variable to False
                        statement = False
                    # creating an elif statement to check if the sum of the users cards is equal to 21
                    elif sum(user_cards) == 21:
                        # printing a message to the user
                        print("You win")
                        # changing the value of the statement variable to False
                        statement = False
                # creating an elif statement to check if the user wants to pass 
                elif response == 'n':
                    # selecting 2 random numbers from the cards list
                    computer_cards = sample(cards, 2)
                    # printing the users cards and the sum of the users cards
                    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                    # printing the users final card and the sum of the computers cards
                    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                    # creating an if statement to check if the sum of the users cards is greater than the sum of the computers cards and the sum of the users cards is less than or equal to 21
                    if sum(user_cards) > sum(computer_cards) and sum(user_cards) <= 21:
                        print("You win")
                        statement = False
                    # creating an elif statement to check if the sum of the computers cards is greater than the sum of the users cards and the sum of the computers cards is less than or equal to 21
                    elif sum(user_cards) < sum(computer_cards) and sum(computer_cards) <= 21:
                        print("Computer wins")
                        statement = False
                    # creating an else statement to check if the sum of the users cards is equal to the sum of the computers cards
                    else:
                        print("It's a draw")
                        statement = False
                # creating an else statement to check if the user input is invalid
                else:
                    print("Invalid input")
                    statement = False
            # asking the user if they want to play a game of blackjack
            choix = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            # creating an if statement to check if the user wants to play a game of blackjack
            if choix == 'y':
                # calling the deal_card function
                deal_card()
            # creating an elif statement to check if the user does not want to play a game of blackjack
            else:
                # changing the value of the users_choice variable to False
                users_choice = False
                # clearing the terminal
                system("clear")
                

# calling the deal_card function
deal_card()
