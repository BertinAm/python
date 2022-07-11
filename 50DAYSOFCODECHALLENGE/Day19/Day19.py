# Day19: 50daysofcodechallenge
def count_words(phrase):
    word = len(phrase.split())
    return f"{word} words"


print(count_words(input("Enter a phrase \n")))


def count_elements(phrase):
    count = 0
    word = phrase.replace(" ", "")
    for word in word:
        count += 1
    return f"{count} elements"


print(count_elements(input("Enter a phrase \n")))

