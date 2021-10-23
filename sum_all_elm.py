def add_all(numbers):
    add = 0
    for num in numbers:
        if num % 2 == 0:
            continue
        add += num
    return(add)
print(add_all([2, 1,1,3,1,3,3,2]))

