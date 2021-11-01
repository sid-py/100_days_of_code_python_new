from turtle import Turtle
import turtle


class Ship(turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.color("green")
        self.penup()
        self.goto(position)
        
        
    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())
        
    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
        