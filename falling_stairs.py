import turtle as turt  # calling the turtle module


def square(animal, size):   # Defining the falling_square function
    for i in range(30):
        animal.fd(size)
        size += 10     # incrementing the size of the square each time it passes through the loop
        animal.lt(90)


sc = turt.Screen()
sc.title("Turtle Square")   # naming the canvas
sc.bgcolor("Green")     # setting the background color of the canvas

alex = turt.Turtle()   # creating the turtle
print(square(alex, 50))  # calling the function and passing into it arguments
sc.mainloop()
