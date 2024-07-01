import turtle as t
import random

turtle_1 = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle_1.color(random_color())
        turtle_1.circle(100)
        turtle_1.setheading(turtle_1.heading() + size_of_gap)

draw_spirograph(5)


