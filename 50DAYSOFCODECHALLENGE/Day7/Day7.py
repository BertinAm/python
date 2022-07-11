def string_range(num):  # creating a function called string_range
    n = -1     # initialising an integer n
    while n < num:  # checking if the number is less than the inputted number
        n += 1   # incrementing the number every time if the number is less than inputted number
        num_string = str(n)   # converting the number into a string
        print(num_string, end=".")  # printing the range of the inputted number


print(string_range(int(input("Enter a number \n"))))



