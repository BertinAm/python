# Day5 of 100DaysOfPython
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
password = ""
# for loop to interate through the lenght of the number of letters entered
for char in range(1, nr_letters + 1):
  # selecting random items from the list letters
  password += random.choice(letters)
# for loop to interate through the lenght of the number of symbols entered
  for char in range(1, nr_symbols + 1):
        # selecting random items from the list symbols
   password += random.choice(symbols)
# for loop to interate through the lenght of the number of numbers entered
   for char in range(1, nr_numbers + 1):
        # selecting random items from the list numbers
    password += random.choice(numbers)
# printing the password
print(password)

#Hard Level
password_list = []
# for loop to interate through the lenght of the number of letters entered
for char in range(1, nr_letters + 1):
    # selecting random items from the list letters
  password_list.append(random.choice(letters))
# for loop to interate through the lenght of the number of symbols entered
for char in range(1, nr_symbols + 1):
  # selecting random items from the list symbols
  password_list += random.choice(symbols)
# for loop to interate through the lenght of the number of numbers entered
for char in range(1, nr_numbers + 1):
  # selecting random items from the list numbers
  password_list += random.choice(numbers)
# printing the password list
print(password_list)
# shuffling the password list
random.shuffle(password_list)
# printing the password list
print(password_list)
# creating an empty string
password = ""
# for loop to interate through the lenght of the password list
for char in password_list:
  # adding the items from the password list to the empty string
  password += char
# printing the password
print(f"Your password is: {password}")