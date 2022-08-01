def guess_a_number(number):
    import random as rd

    random_number = rd.randrange(1, 100)
    count = 0
    while count <= 3:
        if number == random_number:
            return f"{number} is my number. You won!"
        elif number < random_number:
            return f"{number} is not my number. Too low!"
        elif number > random_number:
            return f"{number} is not my number. Too high!"

        count += 1
    print("You Lose!")


print(guess_a_number(int(input("Guess my number \n"))))
