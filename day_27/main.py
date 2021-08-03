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
my_label.pack(side = "top")

# Buttons

button = tkinter.Button(text="Click Me", command = button_click)
button.pack()

input = tkinter.Entry()
input.pack()
input.get()
my_label.config(text = input)
#  ENtry

















window.mainloop()