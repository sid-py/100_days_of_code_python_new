import tkinter

def button_click():
    # print("I got clicked!")
    # my_label["text"] = "I got clicked!"
    new_text = input.get()
    my_label.config(text= new_text)
    
window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text= " I am a text.", font =("Arial", 25, "bold"))
my_label.grid(column=1, row=1)

# Buttons

button = tkinter.Button(text="Click Me", command = button_click)
button.grid(column=2, row=2)

# Button 2

button_2 = tkinter.Button(text="Click Me", command = button_click)
button_2.grid(column=3, row=1)

#  ENtry
input = tkinter.Entry()
input.grid(column=3, row=3)
input.get()
my_label.config(text = input)

















window.mainloop()