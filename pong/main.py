from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# FIXME: Play area is ALMOST adaptable to different-sized screens. Turtle size adapts to the screen.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_R_START = (WINDOW_WIDTH / 2 - 50, 0)
PADDLE_L_START = (-(WINDOW_WIDTH / 2 - 40), 0)
BOUNDARY_TOP = WINDOW_HEIGHT/2 - 10
BOUNDARY_BOTTOM = -(WINDOW_HEIGHT/2 - 20)
BOUNDARY_LEFT = -(WINDOW_WIDTH/2 - 10)
BOUNDARY_RIGHT = WINDOW_WIDTH/2 - 20

screen = Screen()
screen.title("Pong")
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(PADDLE_R_START)
left_paddle = Paddle(PADDLE_L_START)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")
screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision between the top/bottom wall and the ball
    if ball.ycor() == BOUNDARY_TOP or ball.ycor() == BOUNDARY_BOTTOM:
        ball.bounce_y()

    # Detect collision between the ball and the paddles
    if (ball.distance(right_paddle) <= 50 and ball.xcor() >= PADDLE_R_START[0] - 20) \
            or (ball.distance(left_paddle) <= 50 and ball.xcor() <= PADDLE_L_START[0] + 20):
        ball.bounce_x()

    # Ball goes out of bounds
    if ball.xcor() > BOUNDARY_RIGHT:
        ball.reset_position()
        screen.update()
        scoreboard.left_point()
        time.sleep(1)

    elif ball.xcor() < BOUNDARY_LEFT:
        ball.reset_position()
        screen.update()
        scoreboard.right_point()
        time.sleep(1)

screen.exitonclick()
