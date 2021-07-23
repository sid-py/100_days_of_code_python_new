
from ball import Ball
from turtle import Turtle, Screen
import time
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("PONG")
screen.tracer(0)

ball = Ball()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0) )  
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "z")

game_is_on = True
while game_is_on:
    screen.update()












screen.exitonclick()
