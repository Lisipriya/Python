import time
from turtle import Turtle, Screen
from snake import Snake

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)


snake = Snake()
continue_game = True

my_screen.listen()
my_screen.onkey(snake.move_up, "Up")
my_screen.onkey(snake.move_down, "Down")
my_screen.onkey(snake.move_left, "Left")
my_screen.onkey(snake.move_right, "Right")

while continue_game:
    time.sleep(0.1)
    my_screen.update()
    snake.move()


my_screen.exitonclick()
