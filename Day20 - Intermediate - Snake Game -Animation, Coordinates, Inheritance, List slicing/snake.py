from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_body_list = []
        self.form_snake()
        self.snake_head = self.snake_body_list[0]

    def form_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_body_list.append(snake_body)

    def extend_snake(self):
        self.add_segment(self.snake_body_list[-1].position())

    def move_snake(self):
        for i in range(len(self.snake_body_list) - 1, 0, -1):
            new_xcor = self.snake_body_list[i - 1].xcor()
            new_ycor = self.snake_body_list[i - 1].ycor()
            self.snake_body_list[i].goto(new_xcor, new_ycor)
        self.snake_body_list[0].forward(FORWARD_DISTANCE)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
