from turtle import Turtle, Screen, colormode
import random
coco = Turtle()
visual = Screen()
coco.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


i = 0
colormode(255)
while i < 80:
    coco.speed("fastest")
    coco.circle(100)
    coco.color(random_color())
    coco.left(5)
    i += 1

#2nd method
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         coco.color(random_color())
#         coco.circle(100)
#         coco.setheading(coco.heading() + size_of_gap)
# draw_spirograph(5)

visual.exitonclick()
