def compare(a, b):
    if a > b:
        print(a, "is greater than", b)
        return 1
    elif a == b:
        print(a, "is equal to", b)
        return 0
    elif a < b:
        print(b, "is greater than", a)
        return -1
    else:
        return "Wrong entry"


print(compare(float(input("Enter a number \n")), float(input("Enter a number\n"))))
