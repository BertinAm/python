# Day37: 50daysofcodechallenge
def count_the_vowels(word):      # defining the function

    lowercase_word = word.lower()     # converting whatever string entered by the user to lower case
    duplicate_free_word = list(dict.fromkeys(lowercase_word))    # removing duplicate vowels and letters
    vowel = "aeiou"   # assigning the vowels to the variable vowel
    empty_list = []    # creating an empty list
    for iterated_word in duplicate_free_word:   # iterating through the list duplicate_free_word
        for iterated_vowel in vowel:   # iterating through thr string vowel
            w = iterated_word.count(iterated_vowel)    # counting all the vowels in the word
            empty_list.append(w)   # adding the counted vowels to the empty list

    answer = f"{empty_list.count(1)} vowels"
    return answer      # printing out the vowels found


print(count_the_vowels(input("Enter a word to see how many vowels are in it \n").lower()))      # calling the function


