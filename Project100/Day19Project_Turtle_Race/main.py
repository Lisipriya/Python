from turtle import Turtle, Screen
from random import randint

# tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(height=400, width=500)
colors = ["Red", "Blue", "Orange", "Maroon", "Green", "Magenta"]
user_bet = screen.textinput(
    "Make your own bet:", "Which turtle will win the race "
                          "(Red, Blue, Orange, Maroon, Green,Magenta)? \n Enter a color: ")
my_turtles = []
y_coordinate = [-100, -50, 0, 50, 100, 150]
loop_value = range(0, len(colors))
for items in loop_value:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[items])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate[items])
    my_turtles.append(new_turtle)

if user_bet:
    continue_race = True


while continue_race:

    for turtle_racer in my_turtles:
        if turtle_racer.xcor() > 230:
            continue_race = False
            Winner_racer = turtle_racer.pencolor()
            if Winner_racer == user_bet:
                print(f"You Won the race 🏁 !!! The Winning turtle is {Winner_racer} turtle")
            else:
                print(f"You lost the race 😔 !!! The Winning turtle is {Winner_racer} turtle")

        random_movement_to_race = randint(0, 10)
        turtle_racer.forward(random_movement_to_race)

screen.exitonclick()
