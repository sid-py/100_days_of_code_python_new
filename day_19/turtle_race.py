from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400)
screen.bgcolor("grey")
colors = ["red", "orange", "black", "green", "blue", "purple"]
user_bet = screen.textinput(title = "Make your bet.", prompt = f"Which turtle will win the race? Enter a color from {colors} : ")
y_pos = [-70,-40,-10,20,50,80]

is_race_on = False

all_turtles = []  
for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[turtle_index])
    all_turtles.append(new_turtle) 
            
if user_bet:
    is_race_on = True

while is_race_on:
    for a_turtle in all_turtles:
        if a_turtle.xcor() > 230:
            is_race_on = False
            winning_color = a_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!") 
        rand_distance = random.randint(0,10)
        a_turtle.forward(rand_distance)
       
       
screen.exitonclick()