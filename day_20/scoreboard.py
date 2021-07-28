from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Arial", 24, "normal")
 
    

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open(r"C:\Users\2kjph5\OneDrive - Merit Automotive Electronics Systems, S.L\03-Miscellaneous\Studies\Learning\python\100_days_of_code_python_new\day_20\data.txt",mode= "r+") as data:
            self.highscore = int(data.read())
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.write(f"Score = {self.score} High Score: {self.highscore}", align = ALIGNMENT, font = FONT) 
    
    def reset(self):
        if self.score > self.highscore:
            file.write(self.score)
        self.clear()    
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        

        