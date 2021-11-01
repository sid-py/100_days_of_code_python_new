from turtle import Turtle

class Ship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("spaceship2.gif")
        self.color("green")
        self.penup()
        self.goto(0,-230)
             
        
    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())
        
    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
        