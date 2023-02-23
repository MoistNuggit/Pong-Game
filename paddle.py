from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(position)
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def move_up(self):
        y_cor = self.ycor()
        self.sety(y_cor+10)

    def move_down(self):
        y_cor = self.ycor()
        self.sety(y_cor -10)