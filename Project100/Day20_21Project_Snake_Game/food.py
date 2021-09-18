from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food_pos()

    def refresh_food_pos(self):
        random_x_cor = randint(-260, 260)
        random_y_cor = randint(-240, 240)
        self.goto(random_x_cor, random_y_cor)
