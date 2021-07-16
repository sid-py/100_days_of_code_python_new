from turtle import Turtle, Screen
import turtle
import random
timmy = Turtle()




colors = ["royal blue", "dark green", "red", "purple", "lime"] 

turtle_movements = [timmy.forward(100),timmy.left(90),timmy.backward(100),timmy.right(90)]
def timmy_walk():
    for i in random.choice(turtle_movements):
        

for _ in range(10):
    timmy.pensize(10)
    timmy.color(random.choice(colors))
    for i in range(10):
        random.choice(turtle_movements)





screen = Screen()
screen.exitonclick()
