# Day2 of 100DaysOfPython
# Greeting from my program
print("Welcome to the tip calculator!")
# Asking the user for the total bill
bill = float(input("What was the total bill? $"))
# Asking the user the percentage of the tip they are willing to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100 
#Asking the user for the number of people that are to split the bill
number_of_people = int(input("How many people to split the bill? "))
#Getting the the amount each person will pay
amount_for_each_person = bill / number_of_people
#Getting the amount to be tiped by each person
amount_for_each_person_plus_tip = (amount_for_each_person * tip) + amount_for_each_person
# printing the total amount to be tiped
print(f"Each person should pay: {round(amount_for_each_person_plus_tip, 2)}")
