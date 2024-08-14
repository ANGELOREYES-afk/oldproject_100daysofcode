from turtle import Turtle

Font = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=Font)

    def increase(self):
        self.level += 1
        self.update()

    def game(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align="center", font=Font)
