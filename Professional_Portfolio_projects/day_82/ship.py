from turtle import Turtle

class Ship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(position)
             
        
    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())
        
    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
        