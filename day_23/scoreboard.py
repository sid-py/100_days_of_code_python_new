from hashlib import algorithms_available
from turtle import Turtle



FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT) 


    def level(self):
        self.goto(-280 , 280)
        self.write(f"Level: {self.level_num}", align = "left", font = FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()