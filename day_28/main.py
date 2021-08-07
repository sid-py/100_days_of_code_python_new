import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

TICK = "✓"

BUTTON_FONT_SIZE= (FONT_NAME, 8)

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text = count)
    if count > 0:
        window.after(1000, count_down, count - 1 )
    

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

button = tk.Button(text="Start", command = start_timer, font = BUTTON_FONT_SIZE, highlightthickness=0)
button.grid(column=2, row=5)

def reset():
    pass
button = tk.Button(text="Reset", command = reset, font = BUTTON_FONT_SIZE, highlightthickness= 0)
button.grid(column=4, row=5)








window.mainloop()