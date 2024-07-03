from turtle import Turtle, Screen

turtle_1 = Turtle()
screen = Screen()


def move_forward():
    turtle_1.forward(10)


def move_backward():
    turtle_1.backward(10)


def turn_left():
    turtle_1.left(10)


def turn_right():
    turtle_1.right(10)


def clear():
    turtle_1.clear()
    turtle_1.penup()
    turtle_1.home()
    turtle_1.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
