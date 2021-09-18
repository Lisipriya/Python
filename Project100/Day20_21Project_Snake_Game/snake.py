import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend_segment(self):
        self.add_segments(self.snakes[-1].position())

    def move(self):
        for segment in range(len(self.snakes) - 1, 0, -1):
            x_coordinate = self.snakes[segment - 1].xcor()
            y_coordinate = self.snakes[segment - 1].ycor()
            time.sleep(0.01)
            self.snakes[segment].goto(x_coordinate, y_coordinate)
        self.snakes[0].forward(MOVE_FORWARD)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
