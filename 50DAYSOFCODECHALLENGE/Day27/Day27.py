# Day27: 50daysofcodechallenge
def unique_numbers(l):
    from collections import Counter

    cc = Counter(l)
    unq = []
    for x in l:
        if cc[x] > 1:
            unq.append(x)
    var1 = sum(l)
    var2 = sum(unq)
    diff = var1 - var2
    if diff % 2 == 0:
        return l
    else:
        return unq


ll = [1, 2, 4, 5, 6, 7, 8, 8]
print(unique_numbers(ll))
