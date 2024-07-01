# use the below code to extract colors from image in the form of rgb values
# import colorgram
#
# rgb_values = []
# colors = colorgram.extract("hirst_spot_painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_values.append(new_color)
#
# print(rgb_values)

from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
turtle_1 = Turtle()
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
              (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]


# To hide the trail of turtle
turtle_1.penup()

# To hide the turtle
turtle_1.hideturtle()

turtle_1.setposition(-200, -200)
num_of_dots = 100
for dots_count in range(1, num_of_dots + 1):
    turtle_1.dot(20, random.choice(color_list))
    turtle_1.forward(50)

    if dots_count % 10 == 0:
        turtle_1.left(90)
        turtle_1.forward(50)
        turtle_1.left(90)
        turtle_1.forward(500)
        turtle_1.setheading(0)

screen = Screen()
screen.exitonclick()