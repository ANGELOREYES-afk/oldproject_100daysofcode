from turtle import Turtle
import random

colors = ["red", "orange", "yellow","green", "blue", "purple"]
start = 1
move = 3


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = start

    def create(self):
        random_choice = random.randint(1, 6)
        if random_choice == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level(self):
        self.car_speed += move
