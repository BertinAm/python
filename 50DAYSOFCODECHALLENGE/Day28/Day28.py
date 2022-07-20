# Day28: 50daysofcodechallenge
def index_position(word):
    c = 0
    empty = []
    for b in word:
        if b.islower():
            c += 1
            empty.append(c)
    return empty


print(index_position(input("Enter a word \n")))
