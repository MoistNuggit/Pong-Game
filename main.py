from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
scoreboard = Scoreboard()

screen.listen()

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
# screen.onkeypress(fun=right_paddle.move_up,key="Up")
# screen.onkeypress(fun=right_paddle.move_down,key="Down")
# screen.onkeypress(fun=left_paddle.move_down,key="s")
# screen.onkeypress(fun=left_paddle.move_up,key="w")


def tick():
    for action in keys_pressed:
        actions[action]()
    screen.update()
    screen.ontimer(tick, frame_delay_ms)


frame_delay_ms = 1000//30
actions = dict(
    l_u=lambda :left_paddle.move_up(),
    l_d = lambda : left_paddle.move_down(),
    r_u=lambda : right_paddle.move_up(),
    r_d=lambda :right_paddle.move_down(),
)
keys_pressed = set()
screen.onkeypress(lambda :keys_pressed.add("l_u"), "w")
screen.onkeypress(lambda :keys_pressed.add("l_d"), "s")
screen.onkeypress(lambda :keys_pressed.add("r_u"), "Up")
screen.onkeypress(lambda :keys_pressed.add("r_d"), "Down")
screen.onkeyrelease(lambda: keys_pressed.remove("l_u"), "w")
screen.onkeyrelease(lambda: keys_pressed.remove("l_d"), "s")
screen.onkeyrelease(lambda: keys_pressed.remove("r_u"), "Up")
screen.onkeyrelease(lambda: keys_pressed.remove("r_d"), "Down")
tick()

game_running = True
while game_running:
    screen.update()
    ball.ball_move()

    # DETECT COLLISION WIHT UP AND DOWN WALL
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_from_wall()

#     DETECT COLLISION WITH THE PADDLES
    if ball.distance(right_paddle)<50 and ball.xcor()>=340:
        ball.ball_hit()
        ball.speed_up()
    if ball.distance(left_paddle)<50 and ball.xcor()<= -340:
        ball.ball_hit()
        ball.speed_up()

    # DETECT WHEN BALL HITS SIDE(LEFT RIGHT) WALLS
    # IF IT HITS ITS GG GAME OVER
    # BELOW IS WHEN RIGHT PADDLE MISSES AND LEFT SCORES
    if ball.xcor() >= 380:
        ball.ball_hit()
        ball.reset_position()
        scoreboard.left_scores()

    # BELOW IS WHEN LEFT PADDLE MISSES AND RIGHT SCORES
    if ball.xcor() <= -380:
        ball.ball_hit()
        ball.reset_position()
        scoreboard.right_scores()



screen.exitonclick()