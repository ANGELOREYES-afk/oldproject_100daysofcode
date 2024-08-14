import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

is_on = True
while is_on:
    time.sleep(.01)
    screen.update()
    car_manager.create()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game()
            is_on = False
    if player.is_at():
        player.reset()
        car_manager.level()
        scoreboard.increase()
screen.exitonclick()


