from turtle import Turtle

class Scoreboard:
    
    def __init__(self):
        super().__init__(Turtle)
        self.write("Score = ", True, align = "center", font = ("Arial", 10, "normal"))