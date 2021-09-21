import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        level_up = Turtle()
        level_up.hideturtle()
        level_up.setposition(0, 0)
        level_up.write(f'Congratulations Level up', font=("Courier", 16, "normal"), align='center')
        level_up.clear()
        time.sleep(1)
        self.car_speed += MOVE_INCREMENT

