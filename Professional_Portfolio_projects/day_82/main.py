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
import ship

# -----------------UI INterface-------------------#

screen = Screen()
screen.bgcolor("black")
screen.title("Shoot 'em Up!")
screen.setup(width=500, height=500)

space_ship = ship.Ship((-350,0))















screen.exitonclick()