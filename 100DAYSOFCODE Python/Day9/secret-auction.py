# Day9 100DaysOfCodePython
# Secret Auction Program
# import os module to clear screen
from os import system
# import art module to print logo
import art
# printing logo
print(art.logo)
# printing welcome message
print("Welcome to the secret auction program.")
# creating a function called secret_auction that takes in two parameters, name and bid
def secret_auction(name, bid):
  # creating a variable called more_bidders that stores the string "yes"
  more_bidders = "yes"
  # creating an empty dictionary called bidders
  bidders = {}
  # adding the name and bid to the bidders dictionary
  bidders[name] = bid
  # creating a while loop that runs while the more_bidders variable is equal to "yes"
  while more_bidders == "yes":
    # clearing the screen
    system('clear')
    # asking the user to input their name
    name = input("What is your name?: ")
    # asking the user to input their bid
    bid = int(input("What's your bid? $"))
    # adding the name and bid to the bidders dictionary
    bidders[name] = bid
    # asking the user if there are any other bidders
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.? : ").lower()
  # creating a for loop that loops through the bidders dictionary
  for key in bidders:
    # creating a variable called bids_list that stores the values of the bidders dictionary
    bids_list = bidders.values()
    # creating a variable called value that stores the maximum value in the bids_list
    value = max(bids_list)
    # creating an if statement that checks if the value is equal to the value of the key in the bidders dictionary
    if value == bidders[key]:
      # if the if statement is true, then the key and value are printed
      print(f"The winner is {key} with a bid of ${bidders[key]}")

# asking the user to input their name
names = input("What is your name?: ").lower()
# asking the user to input their bid
bids = int(input("What's your bid? $"))
# calling the secret_auction function and passing in the names and bids as arguments
secret_auction(names, bids) 
    
    
  
