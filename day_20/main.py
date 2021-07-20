from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
  
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    
  























screen.exitonclick()