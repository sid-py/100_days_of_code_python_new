import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move_player, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    
    if player.distance(cars) < 50:
        game_is_on = False
        player.game_over()
    
 
    
    
    
    
    
    
    
screen.exitonclick()
