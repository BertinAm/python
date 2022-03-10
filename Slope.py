def slope(x1, y1, x2, y2):
    value1 = y2 - y1
    value2 = x2 - x1
    result = value1 / value2
    return result


print(slope(float(input("Enter x value 1 \n")), float(input("Enter y value 1 \n")), float(input("Enter x value 2 \n")),
            float(input("Enter y value 2 \n"))))
print(slope)