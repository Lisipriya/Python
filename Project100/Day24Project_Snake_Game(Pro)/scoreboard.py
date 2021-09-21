from turtle import Turtle
FONT = ("Arial", 12, "normal")
ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("file.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.setposition(-10, 250)
        self.color('white')
        self.add_score()
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.write(f'Score: {self.score} and High Score: {self.high_score}', font=FONT, align=ALIGN)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("file.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.add_score()

    def increase_score(self):
        self.score += 1
        self.add_score()

