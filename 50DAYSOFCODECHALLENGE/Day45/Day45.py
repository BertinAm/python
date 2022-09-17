# Day45: 50daysofcodechallenge
def analyse_string(sentence): # creating the function analyse_string
    import string  # importing the string library

    dict1 = {     # creating a dictionary with 3 keys
        "number of special characters": "",
        "number of words": "",
        "number of characters": ""
    }
    count = 0  # creating a variable called count with value 0
    count1 = 0 # creating a variable called count1  with value 0
    special_characters = string.punctuation  # parsing all the special characters as values into the variable special_characters
    letters = string.ascii_letters  # parsing all the letters as values into the variable letters
    for word1 in sentence.split():  # iterating through the variable sentence.split
        for words1 in word1:  # iterating through the variable word1
            words1 = words1.replace('"', ' ')  # replacing all the quotes with whitespace
            if words1 in special_characters:  # checking if they are any special characters in the variable words1
                count += 1  # incrementing
                dict1["number of special characters"] = count  # parsing the incremented value stored in count into the dictionary
    number_of_characters = len(sentence.replace(" ", ""))   # parsing the length of the variable sentence with method replace
    dict1["number of characters"] = number_of_characters # parsing in the value of the variable number_of_characters
    for word2 in sentence.split():
        for words2 in word2:
            words2 = words2.replace(' ', '')
            if words2 in letters:
                count1 += 1
                dict1["number of words"] = count1
    print(dict1)  # printing the dictionary dict1


word = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'   # initialising the variable word

analyse_string(word)  # calling the function analyse_string
