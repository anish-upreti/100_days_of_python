from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"score: {self.left_score}", font=("Arial", 20, "normal"))
        self.goto(100, 250)
        self.write(f"score: {self.right_score}", font=("Arial", 20, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()