def add_all(numbers):
    add = 0
    for num in numbers:
        if num % 2 == 0:
            continue
        add += num
    return(add)
print(add_all([2,3,5,6,8,5,23,7,1]))

