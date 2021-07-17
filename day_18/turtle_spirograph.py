# Importing required modules
from turtle import Turtle, Screen, colormode
import turtle
import random
timmy = Turtle()
turtle.colormode(255)

# Creating function for random colors acc. to RGB colors
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b) 

# Creating list of directions NSEW
directions = [0,90,180,270]

# Setting Turtle speed
timmy.speed("fastest")

for i in range(72):
    timmy.color(random_color())
    timmy.left(5)
    timmy.circle(100)
        
# Screen settings
screen = Screen()
screen.exitonclick()