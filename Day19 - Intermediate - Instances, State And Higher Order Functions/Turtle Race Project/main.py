from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=700, height=500)
user_guess = screen.textinput(title="Make your guess ",
                              prompt="Which  turtle will win the race? Choose a turtle from red, blue, "
                                     "green, black, silver, purple:  ").lower()
colors = ["red", "blue", "green", "black", "purple", "silver"]
y_position = -150
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-340, y=y_position)
    y_position += 50
    turtle_list.append(new_turtle)

if user_guess:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 330:
            win_color = turtle.pencolor()
            if win_color == user_guess:
                print(f"You guessed it right. The {win_color} turtle is the winner.")
            else:
                print(f"You guessed it wrong. The {win_color} turtle is the winner.")

            race_on = False
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
