# Still need to work on the formula to mak sure that it gives the answers accurately
def day_add(day, num):

    later_day = int(input(" Enter the day you wish to go on the trip eg 19 or whatever \n"))
    result = (abs(num - later_day) // 30)
    if result == 0:
        print("Your going on a " + " Monday")
    elif result == 1:
        print("Your going on a " + " Tuesday")
    elif result == 2:
        print("Your going on a " + " Wednesday")
    elif result == 3:
        print("Your going on a " + " Thursday")
    elif result == 4:
        print("Your going on a " + " Friday")
    elif result == 5:
        print("Your going on a " + " Saturday")
    elif result == 6:
        print("Your going on a " + " Sunday")
    else:
        print("Non Valid!")


print(day_add(input("Enter any day of the week \n"), int(input("Enter the day your in eg 24 of march etc \n"))))
