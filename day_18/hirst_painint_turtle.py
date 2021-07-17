import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

colors = [(239, 230, 221), (0, 0, 0), (231, 153, 82), (119, 171, 203), (39, 110, 159), (240, 200, 80), (160, 59, 83), (200, 83, 
111), (215, 132, 159), (23, 137, 102), (223, 83, 61), (119, 189, 154), (158, 164, 48), (188, 212, 222), (244, 156, 174), (47, 171, 134), (230, 197, 214), (28, 164, 194), (197, 221, 212), (161, 74, 52), (9, 102, 78), (242, 164, 153), (115, 43, 56), (108, 115, 171), (151, 214, 194), (148, 208, 225), (178, 181, 215), (42, 60, 103), (110, 46, 44), (34, 66, 83)]
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

num_dots = 100
for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()