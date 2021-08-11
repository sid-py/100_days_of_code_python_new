import tkinter as tk
import math
from typing import Text

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

TICK = "✓"

BUTTON_FONT_SIZE= (FONT_NAME, 8)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text = "00:00")
    # title_label "Timer"
    label.config(text = "Timer", fg = GREEN)
    
    global reps
    reps = 0
    
    # reset check marks
    tick.config(text = "")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0:
        count_down(long_break_sec)
        label.config(text="Break", fg = RED)
        
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg = PINK)
        
    else:
        count_down(work_sec)
        label.config(text="Work", fg = GREEN)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    # 00:00
    
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
        
    if count_min <= 9:
        count_min = f"0{count_min}"
    
        
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1 )
        
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += TICK
        tick.config(text = marks)
            
    

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=90, pady = 50, bg = YELLOW)




label = tk.Label(text= "Timer", fg = GREEN, bg= YELLOW, font = (FONT_NAME, 40, "bold" ) )
label.grid(column = 3, row = 0)
canvas = tk.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tk.PhotoImage(file = r"day_28\tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 3, row = 3)


#  Adding a tick mark for each 25 mins loop
tick = tk.Label(text = TICK, fg = GREEN, bg=YELLOW, font =(FONT_NAME, 10, "bold") )
tick.grid(column=3, row=6)

# Defining the functions for the buttons

start_button = tk.Button(text="Start", command = start_timer, font = BUTTON_FONT_SIZE, highlightthickness=0)
start_button.grid(column=2, row=5)

reset_button = tk.Button(text="Reset", command = reset_timer, font = BUTTON_FONT_SIZE, highlightthickness= 0)
reset_button.grid(column=4, row=5)








window.mainloop()