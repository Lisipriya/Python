from turtle import Turtle, Screen, colormode
from random import randint

coco = Turtle()
coco.shape("turtle")

def draw_shapes(num_of_sides):
    sides = 0
    while sides < num_of_sides:
        coco.forward(100)
        coco.right(360/num_of_sides)
        sides += 1


colormode(255)
num_of_sides = 3
while num_of_sides < 11:
    draw_shapes(num_of_sides)
    coco.color(randint(0, 255), randint(0, 255), randint(0, 255))
    if num_of_sides == 10:
        for i in range(6):
            coco.forward(100)
            coco.right(36)
        coco.right(90)
        coco.right(90)
        # coco.setheading(180)
        coco.circle(200)
    num_of_sides += 1


on_screen = Screen()
on_screen.exitonclick()
