from turtle import Turtle

class Bullet(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.1)
        self.color("red")
        self.penup()
        
        
    def fire_bullet(self):
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10
        self.goto(new_x, new_y)
        
        