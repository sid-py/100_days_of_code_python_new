from turtle import Turtle, Screen
import turtle
import random
timmy = Turtle()


def draw_figure(sides):
    return 360/sides

colors = ["royal blue", "dark green", "red", "purple", "lime"] 

n = 2
for i in range(9):
    n+=1
    timmy.color(random.choice(colors))
    for _ in range(n):
        timmy.forward(100)
        timmy.right(draw_figure(n))


screen = Screen()
screen.exitonclick()
