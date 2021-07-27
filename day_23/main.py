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
    
    cars.create_car()
    cars.move_car()
    
    # Detect collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.game_over()
    
    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()
    
 
    
    
    
    
    
    
    
screen.exitonclick()
