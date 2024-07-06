from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            data = int(file.read())
        self.highscore = data
        self.hideturtle()
        self.penup()
        self.goto(0, 320)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
