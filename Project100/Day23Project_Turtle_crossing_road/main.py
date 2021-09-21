import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_class = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
continue_game = True
while continue_game:
    time.sleep(0.1)
    screen.update()
    car_class.create_car()
    car_class.move_cars()

    # Detect turtle collision with the cars
    for car in car_class.cars:
        if car.distance(player) < 20:
            continue_game = False
            score.game_over()

    # Detect the turtle has reached the top
    if player.reached_finish_line_y():
        player.go_to_start()
        score.add_level()
        car_class.level_up()

screen.exitonclick()