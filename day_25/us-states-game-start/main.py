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

while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50", prompt = "What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


states_to_learn = all_states - guessed_state
print(states_to_learn)
# states_to_learn.csv
















screen.exitonclick()