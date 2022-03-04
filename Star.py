import turtle as turt


def draw_star(animal, size):
    for _ in range(5):
        animal.fd(size)
        animal.rt(144)


sc = turt.Screen()
sc.title("STAR")
sc.bgcolor("Green")

alex = turt.Turtle()
print(draw_star(alex, 100))
sc.mainloop()
