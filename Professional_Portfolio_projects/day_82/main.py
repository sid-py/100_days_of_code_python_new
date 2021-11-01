""" A classic Arcade game SHoot em Up! """

# TODO 1: Insert an image of an Alien
# TODO 2: Insert an image of a space ship
# TODO 3: MAke multiple copies of the aliens
# TODO 4: Make the ship movable along X axis
# TODO 5: Add bullets to the space ship
# TODO 6: MAke the bullets to be fired
# TODO 7: Detect contact between bullet and alien
# TODO 8: Make alien disappear after hit
# TODO 9: Move the alien array downward step by step
# TODO 10: Detect alien to space ship contact == GAME OVER.
# TODO 11: Additional features: Levelling up after all space ship destruction


# import tkinter as tk
from turtle import Turtle, Screen
from ship import Ship
from bullet import Bullet
import time

# -----------------UI INterface-------------------#
# SPACE_SHIP_LOC = r"C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\Professional_Portfolio_projects\day_82\spaceship2.gif"

SPACE_SHIP_STARTING_POSITION = (0,-230)


screen = Screen()
screen.bgcolor("black")
screen.title("Shoot 'em Up!")
screen.setup(width=500, height=500)
screen.tracer(5)
bullet = Bullet()
screen.tracer(5)
space_ship = Ship(SPACE_SHIP_STARTING_POSITION)

screen.listen()
screen.onkeypress(space_ship.go_left, "Left")
screen.onkeypress(space_ship.go_right, "Right")

game_is_on = True

while game_is_on:
    
    time.sleep(bullet.fire_bullet)
    screen.update()
    
    
    

















screen.exitonclick()