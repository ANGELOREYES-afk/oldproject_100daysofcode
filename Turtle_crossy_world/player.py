from turtle import Turtle

Start = (0, -280)
move = 10
finish_y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(Start)
        self.setheading(90)

    def go_up(self):
        self.forward(move)

    def is_at(self):
        if self.ycor() > finish_y:
            return True
        return False

    def reset(self):
        self.goto(Start)
