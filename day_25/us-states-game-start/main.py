"""
This game shows a map of USA and prompts the user to guess the name of states. If the name is correct, it is shown 
on the map. If entered "Exit", the game ends and the list of remaining states are saved in a separate .csv file
as an aid for the user to learn and improve the name of states.

The game if programmed through Python's Turtle module.
"""

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Path for the image
image = r"day_25\us-states-game-start\blank_states_img.gif"

# Adding shape in turtle as the image
screen.addshape(image)

# Loading image on the turtle game
turtle.shape(image) 

data = pd.read_csv(r"day_25\us-states-game-start\50_states.csv")
all_states = data["state"].to_list()
guessed_state =[]
missing_states = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50", prompt = "What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(r"day_25\us-states-game-start\states_to_learn.csv")        
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




















screen.exitonclick()