def turn_clockwise(points):
    if points == "N":
        print("E")
    elif points == "E":
        print("S")
    elif points == "S":
        print("W")
    elif points == "W":
        print("N")
    else:
        return "wrong input!"


print(turn_clockwise(input("Please enter a cardinal point to see the next clockwise point i.e N = E \n")))
