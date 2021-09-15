from turtle import Turtle, Screen


coco = Turtle()
coco.shape("turtle")
# coco.color("red", "green")
#
# i = 0
# while i < 15:
#     coco.forward(10)
#     coco.penup()
#     coco.forward(10)
#     coco.pendown()
#     i += 1

coco.forward(100)
coco.penup()
coco.goto(0, 50)
coco.setheading(90)
coco.pendown()


on_screen = Screen()
on_screen.exitonclick()
