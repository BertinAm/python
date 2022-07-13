# Day23: 50daysofcodechallenge
try:
    print("welcome am a calculator you can perform your operations in the next line")
    operation = eval(input(""))
    print(operation)
except ValueError:
    print("can't perform operations between str and int\n")
except TypeError:
    print("unsupported operand type(s)\n")
except ZeroDivisionError:
    print("You can't divide a number by zero \n")


