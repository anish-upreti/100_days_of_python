import time
from turtle import Screen
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

our_turtle = Player()
game_car = Car()
scoreboard = Score()

screen.listen()
screen.onkey(our_turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    game_car.produce_car()
    game_car.move_car()

    # Detect collision with car
    for car in game_car.all_cars:
        if car.distance(our_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # When the turtle reach other end
    if our_turtle.at_other_end():
        our_turtle.restart()
        game_car.speed_up()
        scoreboard.increase_level()


screen.exitonclick()
