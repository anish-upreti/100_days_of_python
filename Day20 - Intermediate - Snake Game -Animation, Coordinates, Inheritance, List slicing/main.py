from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(height=700, width=700)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake_1 = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake_1.left, "Left")
screen.onkey(snake_1.right, "Right")
screen.onkey(snake_1.up, "Up")
screen.onkey(snake_1.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake_1.move_snake()

    # Detect collision with food
    if snake_1.snake_head.distance(food) < 15:
        food.rand_location()
        snake_1.extend_snake()
        scoreboard.increase_score()

    # Detect collision with food
    if snake_1.snake_head.xcor() > 340 or snake_1.snake_head.xcor() < -340 or snake_1.snake_head.ycor() > 340 or snake_1.snake_head.ycor() < -340:
        game_on = False
        scoreboard.game_over()

    # Detect collision with snake body
    for body_part in snake_1.snake_body_list[1:]:
        if snake_1.snake_head.distance(body_part) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
