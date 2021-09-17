import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()

my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

    # Detect the food
    if snake.head.distance(food) < 15:
        food.refresh_food_pos()
        snake.extend_segment()
        scoreboard.add_score()

    # Detect collision with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        continue_game = False
        scoreboard.game_over()

    # Detect collision with its own tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            continue_game = False
            scoreboard.game_over()

my_screen.exitonclick()
