# Day20: 50daysofcodechallenge
def capitalize(word):
    a = word.split()
    for b in a:
        print(b.capitalize(), end=" ")


phrase = input("Enter a phrase \n")
capitalize(phrase)


