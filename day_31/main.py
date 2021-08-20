import tkinter as tk
from typing import Text
import pandas as pd
import random
import time

# Global variables definition

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# Error handling

try:
    data = pd.read_csv(r"day_31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"day_31\data\deutsch_to_eng_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Flash card main function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card =random.choice(to_learn)
    canvas.itemconfig(card_background, image = card_front_img)
    canvas.itemconfig(card_title, text = "Deutsch", fill ="black")
    canvas.itemconfig(card_word, text = current_card["Deutsch"], fill ="black" )
    window.after(3000, func = flip_card)

# Card flipping functionality 
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "White")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "White" )
    canvas.itemconfig(card_background, image = card_back_img)

# Removes the word from the list and saves it in a separate file 
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"day_31\data\words_to_learn.csv", index = False)
    next_card()
        
# Creating Window

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

# Flipping timer after which the card "flashes" automatically
flip_timer = window.after(3000, func = flip_card)

# All Images
right_img = tk.PhotoImage(file = r"day_31\images\right.png")
wrong_img = tk.PhotoImage(file = r"day_31\images\wrong.png")
card_front_img = tk.PhotoImage(file = r"day_31\images\card_front.png")
card_back_img = tk.PhotoImage(file = r"day_31\images\card_back.png")

# Canvas definition
canvas = tk.Canvas(width=800, height=526)
card_background = canvas.create_image(400,263, image = card_front_img)
card_title = canvas.create_text(400,150, text = "", font = ("Arial", 40, "italic"))
card_word = canvas.create_text(400,280, text = "", font = ("Arial", 60, "bold"))

canvas.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(column=0, row=0, columnspan=2)

# Adding the right button
right_button = tk.Button(image=right_img, highlightthickness=0, command = is_known)
right_button.grid(column=0, row=1)

# Adding the Wrong button
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command = next_card)
wrong_button.grid(column=1, row=1)

# Function takes care of the next card
next_card()
    

# Window mainloop  
window.mainloop()