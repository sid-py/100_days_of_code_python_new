from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
LEVEL_NUM = 1


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
        
    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def finish(self):
        if self.move_player.ycor() == FINISH_LINE_Y:
            self.LEVEL_NUM += 1
            self.goto(STARTING_POSITION)
        

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = "courtier")
        
    
    def level(self):
        self.goto(-280 , 280)
        self.write(f"Level: {LEVEL_NUM}")
        