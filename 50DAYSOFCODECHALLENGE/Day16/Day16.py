# Day16: 50daysofcodechallenge
def sum_list(nested_list):
    empty = []
    for b in nested_list:
        for c in b:
            empty.append(c)
    return sum(empty)


a = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(a))



