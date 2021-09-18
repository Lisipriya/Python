from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("My Pong Game")
my_screen.tracer(0)

left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))
ball = Ball()
score = ScoreBoard()

continue_game = True

my_screen.listen()
my_screen.onkey(left_paddle.move_up, "w")
my_screen.onkey(left_paddle.move_down, "s")
my_screen.onkey(right_paddle.move_up, "Up")
my_screen.onkey(right_paddle.move_down, "Down")

while continue_game:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.refresh_ball_pos()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # continue_game = False

    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect left side ball out of bounds
    if ball.xcor() > 360:
        ball.reset_position()
        score.add_left_score()


    # Detect right side ball out of bounds
    if ball.xcor() < -360:
        ball.reset_position()
        score.add_right_score()




my_screen.exitonclick()