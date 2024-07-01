import turtle as t
import random

turtle_1 = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle_1.pensize(15)
turtle_1.speed("fastest")

for _ in range(200):
    turtle_1.color(random.choice(colours))
    turtle_1.forward(30)
    turtle_1.setheading(random.choice(directions))

