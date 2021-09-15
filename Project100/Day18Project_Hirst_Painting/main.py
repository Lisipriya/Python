import random

import colorgram
from turtle import Turtle, Screen, colormode

# colors_list = colorgram.extract('hirst-painting.jpg', 15)
# picture_colors = []
# for dot_color in colors_list:
#     red = dot_color.rgb.r
#     green = dot_color.rgb.g
#     blue = dot_color.rgb.b
#     combine_colors = (red, green, blue)
#     picture_colors.append(combine_colors)
# print(picture_colors)

coco = Turtle()
visual = Screen()
visual.setup(width=1.0, height=1.0)
coco.speed("fastest")
coco.hideturtle()
picture_colors = [(203, 10, 33), (245, 234, 50), (239, 234, 2), (219, 159, 74), (241, 36, 137), (41, 82, 176),
                  (30, 39, 158), (37, 216, 59), (204, 72, 21), (22, 148, 26), (203, 32, 106)]
colormode(255)


def random_color():
    color = random.choice(picture_colors)
    return color


i = 1
for column in range(0, 10):
    for row in range(0, 10):
        coco.dot(20, random_color())
        coco.penup()
        coco.forward(50)
        coco.pendown()
    coco.penup()
    value = 50*i
    coco.goto(0, value)
    coco.pendown()
    i += 1
visual.exitonclick()
