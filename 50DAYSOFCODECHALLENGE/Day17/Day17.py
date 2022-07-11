# Day17: 50daysofcodechallenge
def user_name(name):
    import random

    a = random.randint(0, 9)
    return f"Your user name is {name[::-1]}{a}"


print(user_name(input("Enter your name \n").lower()))


