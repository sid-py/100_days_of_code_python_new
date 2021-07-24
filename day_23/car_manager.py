from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        for i in COLORS:
            self.color(i)
        self.shape("square")
        self.shapesize(stretch_wid = 0.5, stretch_len= 1)
        self.clone()
        self.penup()
        self.setheading(180)
        
        for i in random.randrange(-280, 280):
            self.sety(i)
        
        
        
    def move(self):
        new_x = self.xcor() + STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())
        
    def speed_increment(self):
        self.move += MOVE_INCREMENT
    
    
        
        
    
