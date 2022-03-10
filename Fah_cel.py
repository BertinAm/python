def f2c(fah):
    val1 = ((fah - 32) * 5) / 9
    return round(val1)


print(f2c(int(input("Enter your fahrenheit temperature to see the corresponding Celsius temperature \n"))))
