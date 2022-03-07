num = int(input("Enter the number of days you wish to stay\n"))
count = 0
while num != 0:
    count += 1
    num = num // 10
    if num // 10 == 1:
        print(" You'll return on a sunday")
    elif num // 10 == 2:
        print("You'll return on a Monday")
    elif num // 10 == 3:
        print("You'll return on a Tuesday")
    elif num // 10 == 4:
        print("You'll return on a Wednesday")
    elif num // 10 == 5:
        print("You'll return on a Thursday")
    elif num // 10 == 6:
        print("You'll return on a Friday")
    elif num // 10 == 7:
        print("You'll return on a Saturday")
    elif num // 10 > 7:
        print("you can't have a vaccation these long!")
        break
