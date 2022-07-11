# Day12: 50daysofcodechallenge
def count_dots(str1):   # defining the function count_dots
    num = str1.count(".")   # counting the number of dots entered the word from the user
    return f"{num} dots"    # printing out the number of dots using f strings


print(count_dots(input("Enter a word with any number of dots for me to count \n")))  # calling the function


