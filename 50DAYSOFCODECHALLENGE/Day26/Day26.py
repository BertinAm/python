# Day26: 50daysofcodechallenge
def sort_words(word):
    b = word.replace(" ", "")
    empty = []
    for c in b:
        empty.append(c)
    empty_sort = sorted(empty)
    empty_sort = list(dict.fromkeys(empty_sort))  # fromkeys method is used to form key value pairs in dictionaries
    return empty_sort


a = input("Enter a phrase or sentence to see it in sorted form \n")
print(sort_words(a))
