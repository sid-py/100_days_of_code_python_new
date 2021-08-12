import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx= 20, pady=20)

canvas = tk.Canvas(width = 200, height = 200, highlightthickness = 0)
lock_img = tk.PhotoImage(file = r"day_29\logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column = 3, row = 3)






window.mainloop()
