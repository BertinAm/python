my_name = "Bertin"
count = 0
while 0 <= count <= 2:
    count += 1
    if input("Guess my Name! \n") == my_name:
        print("You guessed my name in ", count, "guesses!")
        break
    else:
        print("Wrong Guess!")

