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

# Setting Turtle parameters
timmy.pensize(15)
timmy.speed("fast")

# For loop to repeate turtle motion
for _ in range(200):
    timmy.color(random_color()) 
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
        
# Screen settings
screen = Screen()
screen.exitonclick()