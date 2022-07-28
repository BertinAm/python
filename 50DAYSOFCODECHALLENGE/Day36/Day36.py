# Day36: 50daysofcodechallenge
def count(word):         # function definition
    import collections        # importing collections package
    counted_word = collections.Counter(word)      # using the Counter method to count each occurrence of each letter in the word
    counted_word = dict(counted_word)   # typecasting
    return counted_word    # returning the counted word


print(count(input("Enter a word \n")))    # calling the function
