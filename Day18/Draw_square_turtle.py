from turtle import Turtle, Screen


coco = Turtle()
coco.shape("turtle")
coco.color("red", "green")

i = 0
while i < 4:
    coco.forward(100)
    coco.right(90)
    i += 1


on_screen = Screen()
on_screen.exitonclick()
