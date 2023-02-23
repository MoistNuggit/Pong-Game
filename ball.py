from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(5)
        self.shape("circle")
        self.color("white")
        self.x_move = 0.125
        self.y_move = 0.125

    def ball_move(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(x=new_x, y=new_y)


    def bounce_from_wall(self):
        # CHANGES THE Y_MOVE FROM POSITIVE TO NEGATIVE AND
        # VICE VERSA
        self.y_move *= -1

    def ball_hit(self):
        # SAME PRINCIPLE AS BOUNCEFROMWALL, CHANGE X_MOVE FROM POSITIVE TO
        # NEGATIVE AND VICE VERSA SO WHEN THE PADDLE HITS BALL, BALL GOES
        # BACKWARDS IN DIRECTION
        self.x_move *= -1

    def reset_position(self):
        self.x_move = 0.125
        self.y_move = 0.125
        self.goto(0,0)

    def speed_up(self):
        self.x_move *= 1.25
        self.y_move *= 1.25