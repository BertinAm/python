# 55_days_of_python_code
from math import sqrt


def divide_or_square(a):
    if a != 0:
        if a % 5 == 0:
            square = sqrt(a)
        else:
            print("Not divisible by 5")
    return square


print(divide_or_square(int(input("Enter a Number \n"))))
