# Day18: 50daysofcodechallenge
def any_num(number):
    b = number.split(",")
    c = len(b)
    empty = []
    for num in b:
        empty.append(int(num))
    sum_of = sum(empty)
    average = sum_of / c
    return f"The average is {average}"


a = input("Enter any amount of numbers but separate by a comma \n")
print(any_num(a))


