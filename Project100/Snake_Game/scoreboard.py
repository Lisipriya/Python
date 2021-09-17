from turtle import Turtle
FONT = ("Arial", 12, "normal")
ALIGN = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(-10, 250)
        self.color('white')
        self.add_score()
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.write(f'Score: {self.score}', font=FONT, align=ALIGN)
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        self.color('white')
        self.write(f'Game Over!!!', font=FONT, align=ALIGN)
        self.hideturtle()
