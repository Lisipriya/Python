from turtle import Turtle, Screen, colormode
import random

coco = Turtle()
visual = Screen()
coco.shape("turtle")


def random_direction():
    directions = {
        "east": 0,
        "north": 90,
        "west": 180,
        "south": 270
    }
    key = random.choice(list(directions))
    value = directions[key]
    return value


colormode(255)
num_of_movement = 0
while num_of_movement < 250:
    coco.setheading(random_direction())
    coco.pensize(10)
    coco.speed(9)
    coco.forward(20)
    coco.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    num_of_movement += 1

on_screen = Screen()
on_screen.exitonclick()
