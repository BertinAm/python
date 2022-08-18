# Day42: 50daysofcodechallenge
def spelling_checker(word):    # Defining the function spelling_checker
    from textblob import TextBlob    # importing the package Textblob

    wrong_spellx = TextBlob(word)     # parsing the word through the TextBlob method

    # using TextBlob.correct() method
    correct_spellx = wrong_spellx.correct()   # correcting the wrongly spelled word

    if wrong_spellx != correct_spellx:    # checking if the word was wrongly spelled
        print(f"Did you mean to type the word {correct_spellx} \n")     # asking the user if he meant to type the word
        answer = input("Enter yes if you did enter no if you didn't \n").lower()  # asking the user to enter yes or no
        if answer == "no":    # checking if the answer is no
            spelling_checker(input("Enter a word \n").lower())    # calling the function spelling_checker
        elif answer == "yes":    # checking if the answer is yes
            print(f"{correct_spellx}")  # printing out the correct word

    else:
        print(f"{correct_spellx}")   # printing out the word


spelling_checker(input("Enter a word \n").lower())   # calling the function spelling_checker


