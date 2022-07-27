# Day35: 50daysofcodechallenge
def check_pangram(sentence):  # creating the function check_pangram
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # parsing the entire alphabet as a string into the variable alphabet
    for alpha in alphabet:  # iterating through the string alphabet and storing in alpha
        if alpha not in sentence.lower():  # checking if the alphabet is not in the string sentence
            return False  # printing False
    return True  # printing True


print(check_pangram(input("Enter a sentence to check if its a pangram \n")))  # calling the function check_pangram
