from turtle import Turtle
MOVE_DISTANCE = 20
SEGMENT_SIZE = 20
STARTING_POSITIONS = [(0 - SEGMENT_SIZE * i, 0) for i in range(0, 3)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def reset_snake(self):
        for segment in self.body:
            segment.reset()
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def grow(self):
        """Makes the snake grow longer by adding another segment"""
        self.add_segment(self.body[-1].position())

    def move(self):
        """Moves the snake forward"""
        for segment in range(len(self.body)-1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
