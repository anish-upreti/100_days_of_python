from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Game")
screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # When ball goes out of bounds
    if ball.xcor() > 420:
        ball.ball_reset()
        scoreboard.right_point()

    if ball.xcor() < -420:
        ball.ball_reset()
        scoreboard.left_point()


screen.exitonclick()
