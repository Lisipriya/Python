from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.setposition(-280, 260)
        self.add_level()
        self.hideturtle()

    def add_level(self):
        self.clear()
        self.write(f'Level:{self.level}', font=FONT, align='left')
        self.level += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write(f'Game Over!!!', font=FONT, align='center')
        self.hideturtle()
