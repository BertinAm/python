# Day41: 50daysofcodechallenge
def words_with_vowels(word):   # creating a function words_with_vowels
    vowel = "aeiou"     # creating a variable called vowel
    vowel_set = set(vowel)   # converting vowel to a set
    empty_list = []  # creating an empty list
    for wrd in word.split():    # iterating through the word that has been split
        if vowel_set & set(wrd):   # checking if they are any vowels in the words entered by the user
            empty_list.append(wrd)   # appending the words in to the empty list
    print(empty_list)   # printing the empty list


words_with_vowels(input("Enter a sentence to see the words that have vowels \n"))    # calling the function


