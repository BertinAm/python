def c2f(cel):
    val1 = 32 + (cel * 9 / 5)
    return round(val1)


print(c2f(int(input("Enter a temperature in celsius to see the corresponding fahrenheit temperature \n"))))

