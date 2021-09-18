from turtle import Turtle

FONT = ("Courier", 70, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self. update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.left_score}', font=FONT, align="center")
        self.goto(100, 200)
        self.write(f'{self.right_score}', font=FONT, align="center")

    def add_left_score(self):
        self.left_score += 1
        self.update_score()

    def add_right_score(self):
        self.right_score += 1
        self.update_score()


