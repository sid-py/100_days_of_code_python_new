from turtle import Turtle

class Bullet(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.1)
        self.color("red")
        self.penup()
        self.goto(position)
        
    def fire_bullet(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)