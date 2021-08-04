""" This is an interactive widget program to convert Miles to kms."""

# Importing the necessary libraries and modules

import tkinter as tk
from tkinter.constants import END

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text = f"{km}")

#Creating a new window and configurations
window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx = 20, pady=20)
window.minsize(width=250, height=100)


miles_input = tk.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text = "Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text = "is equal to")
is_equal_label.grid(column=0, row=1)

km_label = tk.Label(text = "Km")
km_label.grid(column=2, row=1)

km_result_label = tk.Label(text = "0")
km_result_label.grid(column=1, row=1)

calc_button = tk.Button(text = "Calculate", command = miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()