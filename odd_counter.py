def odd_counter(count,number):
    count = 0
    for num in number:
        if num % 2 == 1:
            count += 1
    return(count)
print(odd_counter(0, [1 , 2, 3, 4 , 5, 6, 7, 8, 9 ,10]))
    