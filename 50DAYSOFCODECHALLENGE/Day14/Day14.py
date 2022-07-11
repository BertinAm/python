# Day14: 50daysofcodechalenge
def flat_list(a):
    empty = []
    for b in a:
        for c in b:
            empty.append(c)
    return empty


print(flat_list([[1, 2, 3, 4, 5]]))


