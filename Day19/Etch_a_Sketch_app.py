from turtle import Turtle, Screen

jerry = Turtle()
view = Screen()


def move_forward():
    jerry.forward(100)


def move_backward():
    jerry.backward(100)


def move_clockwise():
    jerry.right(250)


def move_counterclockwise():
    jerry.left(270)


def clear_screen():
    jerry.reset()


view.onkey(move_forward, "W")
view.onkey(move_backward, "S")
view.onkey(move_counterclockwise, "A")
view.onkey(move_clockwise, "D")
view.onkey(clear_screen, "C")
view.listen()


view.exitonclick()







