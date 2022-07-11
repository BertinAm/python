# Day15: 50daysofcodechallenge
def same_in_reverse(word):
    if word[::-1] == word:
        return True
    else:
        return False


print(same_in_reverse(input("Enter a word \n")))



