# Day25: 50daysofcodechallenge
def all_the_same(a):
    n = len(a)
    if a.count(a[0]) == n:
        return True
    else:
        return False


list_or_tuple = ["Mary", "Mary", "Mary"]
print(all_the_same(list_or_tuple))

