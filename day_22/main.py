
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
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the right paddle
    
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        
    if ball.xcor() < -380:
        ball.reset_position()
        
        
    












screen.exitonclick()
