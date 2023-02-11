# Day4 of 100DaysOfPython
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# Greeting from my program
print("Welcome to my rock - paper - scissors game")
# importing the random module
import random
# Asking the user for his choice
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# creating a choices list that contains the rock, paper and scissors ASCII art
choices = [rock, paper, scissors]
# randomly choosing an item from the choices list
computers_choice =  random.choice(choices)

# if the user chooses rock and the computer chooses scissors the user wins
if choices[users_choice] == computers_choice:
  print("Users choice \n\n")
  print(f"{choices[users_choice]} \n\n")
  print("Computers Choice \n\n")
  print(f"{computers_choice}\n")
  print("It's a draw")
# if the user chooses rock and the computer chooses scissors the user wins
elif choices[users_choice] == paper and  computers_choice == rock:
  print("Users choice \n\n")
  print(f"{choices[users_choice]} \n\n")
  print("Computers Choice \n\n")
  print(f"{computers_choice}\n")
  print("You win")
# if the user chooses scissors and the computer chooses paper the user wins
elif choices[users_choice] == scissors and computers_choice == paper:
  print("Users choice \n\n")
  print(f"{choices[users_choice]} \n\n")
  print("Computers Choice \n\n")
  print(f"{computers_choice}\n")
  print("You Win")
# if the user chooses paper and the computer chooses rock the user wins
elif choices[users_choice] == rock and computers_choice == scissors:
  print("Users choice \n\n")
  print(f"{choices[users_choice]} \n\n")
  print("Computers Choice \n\n")
  print(f"{computers_choice}\n")
  print("You Win")
# if the user chooses any option that can help the computer win the computer wins
else:
  print("Users choice \n\n")
  print(f"{choices[users_choice]} \n\n")
  print("Computers Choice \n\n")
  print(f"{computers_choice}\n")
  print("Computer Wins")
