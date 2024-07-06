from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.rand_location()

    def rand_location(self):
        x_position = random.randint(-320, 320)
        y_position = random.randint(-320, 320)
        self.goto(x_position, y_position)
