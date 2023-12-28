from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.goto(r.randint(-260, 260), r.randint(-260, 260))
