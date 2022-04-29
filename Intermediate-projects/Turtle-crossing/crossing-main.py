# Imports
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create objects from classes
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# Turtle controls,turtle should only be able to move up.
screen.listen()
screen.onkeypress(player.move_up, "Up")

# Game loop to keep the game running
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars and move them towards the left of the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Loop through the all_cars list and compare distance to turtle
    # if turtle is within 20 pxs, stop game
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # If player moves out over top border, reset to starting position
    if player.ycor() > 290:
        player.goto(0, -280)
        # You level up when you make it to the other side and so car speed will increase
        car_manager.increase_speed()
        scoreboard.level += 1
        scoreboard.refresh_level()

screen.exitonclick()
