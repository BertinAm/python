def guess_a_number():
    import random as rd

    random_number = rd.randrange(1, 100)
    count = 0
    while count < 4:
        number = int(input("Guess my number \n"))
        if number == random_number:
            print(f"{number} is my number. You won!")
            break
        elif number < random_number:
            print(f"{number} is not my number. Too low!")
        elif number > random_number:
            print(f"{number} is not my number. Too high!")

        count += 1
    print("You Lose!")


guess_a_number()
