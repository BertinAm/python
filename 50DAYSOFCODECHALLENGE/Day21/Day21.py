# Day21: 50daysofcodechallenge
def make_tuples(a, b):
    c = tuple(zip(a, b))
    return c


list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
print(make_tuples(list_a, list_b))
