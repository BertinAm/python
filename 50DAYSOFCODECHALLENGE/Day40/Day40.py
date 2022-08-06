# Day40: 50daysofcodechallenge
def translate(word):      # creating the function
    length = len(word.split())  # splitting the string the user will enter
    if length <= 1:  # checking if the length of the word is less than or equal to 1
        vowel = 'aeiou'    # creating a variable called vowel which contains all the vowels
        word_list = list(word)  # converting the string into a list
        if word_list[0] in vowel:   # checking if the first letter of the string is a vowel
            print(f"{word}yay")  # printing out the word plus the another string yay
        else:
            word_list = list(word)  # converting the word to a list
            word_list.insert(len(word_list) - 1, word_list.pop(0))   # changing the index position of the
            new_str = "".join(word_list)  # converting the list word_List into a str
            print(f"{new_str}ay")   # printing out the word plus the another string ay
    elif length > 1:
        count = 0  # creating a variable called count
        vowel = 'aeiou'
        while count < len(word.split()):  # checking if the variable count is less than the length words entered by the user
            new_word = word.split()   # splitting the words entered by the user
            new = new_word[count][0]  # selecting all the first letters of all the words in the list new_word
            if new_word[count][0] in vowel:  # checking if the first letters in all the words in the list are vowels
                letter = set(new)   # converting all the first letters of the words in the list to a set
                for wrd in new_word:   # iterating through list new_word
                    if letter & set(wrd):   # performing bit wise operations between letter and set(wrd)
                        print(f"{wrd}yay", end=" ")   # printing out the word plus the another string yay
                        break
            else:
                letters = set(new)
                for wrds in new_word:
                    if letters & set(wrds):    # performing bit wise operations between letters and set(wrds)
                        new_words = wrds[1:] + wrds[0]  # changing the position of each word in the string wrds
                        print(f"{new_words}ay", end=" ")   # printing out the word plus the another string ay
                        break
            count += 1   # incrementing the variable count


translate(input("Enter a word \n").lower())    # calling the function translate
