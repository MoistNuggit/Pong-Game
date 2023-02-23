from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.goto(0,240)
        self.write(f"{self.score_left}     {self.score_right}", False, align="center", font=("Arial", 40, "normal"))


    def left_scores(self):
        self.score_left += 1
        self.clear()
        self.write(f"{self.score_left}     {self.score_right}", False, align="center", font=("Arial", 40, "normal"))

    def right_scores(self):
        self.score_right += 1
        self.clear()
        self.write(f"{self.score_left}     {self.score_right}", False, align="center", font=("Arial ", 40, "normal"))