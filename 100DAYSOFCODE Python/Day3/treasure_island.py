print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
# Asking the user for the direction
direction = input('You"re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()
# if the user goes left enter the if statement
if direction == "left":
  # asking the user whether he or she wants to wait or swim
  command = input('You"ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
  # if the user chooses to wait enter the if statement
  if command == "wait":
    # asking the user to pick a door color
    door_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    # if the user picks red game over
    if door_color == "red":
      print("It's a room full of fire. Game Over.")
      # if the user picks yellow they win
    elif door_color == "yellow":
      print("You found the treasure! You Win!")
      # if the user picks blue they die
    elif door_color == "blue":
      print("You enter a room of beasts. Game Over.")
      # if the user enters a door which doesn't exist game over
    else:
      print("You chose a door that doesn't exist. Game Over.")
  # if the user decides to swim game over
  else:
    print("You get attacked by an angry trout. Game Over.")
# if the user decides to go left they fall into a hole game over
else:
  print("You fell into a hole. Game Over.")
