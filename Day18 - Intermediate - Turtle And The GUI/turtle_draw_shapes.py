import turtle as t
import random

turtle_1 = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle_1.forward(100)
        turtle_1.right(angle)

for shape_side_n in range(3, 10):
    turtle_1.color(random.choice(colours))
    draw_shape(shape_side_n)