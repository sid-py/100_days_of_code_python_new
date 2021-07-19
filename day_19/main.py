from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.setheading(0)
    tim.forward(15)

def backwards():
    tim.setheading(180)
    tim.forward(15)    
    
def upwards():
    tim.setheading(90)
    tim.forward(15)
    
def downwards():
    tim.setheading(270)
    tim.forward(15)

def cw():
    tim.setheading(0)
    tim.circle(25)
    
def ccw():
    tim.setheading(180)
    tim.circle(25)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

       
    
screen.listen()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(cw, "d")
screen.onkey(ccw, "a")
screen.onkey(clear, "c")

screen.exitonclick()
