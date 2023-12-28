from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time
# NOTE: Each turtle is 20x20 pixels
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BOUNDARY_R = WINDOW_WIDTH/2 - 20
BOUNDARY_L = -(WINDOW_WIDTH/2 - 10)
BOUNDARY_Y = WINDOW_HEIGHT/2 - 20

screen = Screen()
screen.tracer(0)
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""Start listening"""
screen.listen()
screen.onkeypress(fun=snake.up, key="w")
screen.onkeypress(fun=snake.down, key="s")
screen.onkeypress(fun=snake.left, key="a")
screen.onkeypress(fun=snake.right, key="d")

game_on = True
print(screen.window_width(), screen.window_height())
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.grow()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > BOUNDARY_R \
            or snake.head.xcor() < BOUNDARY_L \
            or snake.head.ycor() > BOUNDARY_Y \
            or snake.head.ycor() < -BOUNDARY_Y:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail (any part of the body)
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
