# Day22: 50daysofcodechallenge
def add_hash(phrase):
    return phrase.replace(" ", "#")


def add_underscore(phrase):
    return phrase.replace("#", "_")


def remove_underscore(phrase):
    return phrase.replace("_", " ")


print(remove_underscore(add_underscore(add_hash(input("Enter a phrase \n")))))
