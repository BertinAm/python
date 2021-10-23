shape = input("enter one of the following circle, rectangle or square\n")
if shape == "circle":
    pi = 3.14
    radius = int(input("please enter the radius\n"))
    area_circle = pi * radius ** 2
    print("The area of the circle is", area_circle)
elif shape == "rectangle":
    length = int(input("please enter the length of the rectangle\n"))
    width = int(input("please enter the width of the rectangle\n"))
    area_rect = length * width 
    print("The area of the rectangle is", area_rect)
elif shape == "square":
    length = int(input("please enter the length of the square\n"))
    area_sqr = length * length
    print("The area of the square is", area_sqr)
else:
    pass