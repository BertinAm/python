def convert_add(new):
    nw = []
    for new_o in new:
        nw.append(str(new_o))
    print(nw)
    new_o = []
    for new_p in nw:
        new_o.append(int(new_p))
    return "The sum of the entered numbers is ", sum(new_o)


print(convert_add(input("Enter a set of numbers to add eg 12345678 \n")))
