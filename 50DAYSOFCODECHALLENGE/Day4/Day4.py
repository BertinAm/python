# Day4 : 50daysofcodechallenge
def only_floats(a, b):     # defining the function only_floats
    x = 1.1                # creating a float
    c = type(x)            # storing the type value of x
    if type(a) == c and type(b) == c:     # comparing if the 2 numbers are floats
        return 2
    elif type(a) == c or type(b) == c:  # comparing if at least 1 number is a float
        return 1
    else:                               # if all numbers are not floats
        return 0


print(only_floats(12.1, 23))          # calling the function
