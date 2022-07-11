# Day11: 50daysofcodechallenge
def equal_strings(str1, str2):       # defined the function equal_strings
    if len(str1) == len(str2) and str1 == str2[::-1] or str2 == str1[::-1]:   # checking if both words are equal in
        # length and number of characters
        return True
    else:
        return False


print(equal_strings(input("Enter a word \n"), input("Enter another word \n")))  # calling the function





