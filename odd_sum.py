def sum(numbers):
    add = 0
    for num in numbers:
        if num % 2 == 1:
            add += num
            continue
    return(add)
print(sum([1, 3, 1, 2, 4, 5]))