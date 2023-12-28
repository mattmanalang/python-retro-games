from turtle import Turtle
# NOTE: The size of the ball is 20x20px
START_SPEED = 0.03

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_speed = 5
        self.y_speed = 5
        self.move_speed = START_SPEED
        self.shape("circle")
        self.color("white")
        self.penup()

    def reset_position(self):
        self.move_speed = START_SPEED
        self.goto(0, 0)
        self.bounce_x()

    def move(self):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.move_speed *= 0.75
        self.x_speed *= -1
