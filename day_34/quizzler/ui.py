import tkinter as tk
from typing import Text
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain = QuizBrain):
        self.quiz = quiz_brain
        
        self.window =tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20, bg=THEME_COLOR)
        # Creation of Score Label
        self.score_label = tk.Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Creation of Canvas
        self.canvas = tk.Canvas(height=250, width=300, bg = "white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text = "Some Question Text", 
            fill = THEME_COLOR, 
            font=("arial", 20, "italic")
            )
        self.canvas.grid(column=0, row=1, columnspan=2)
        true_image = tk.PhotoImage(file = r"day_34\quizzler\images\true.png")
        self.true_button = tk.Button(image = true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        
        false_image = tk.PhotoImage(file = r"day_34\quizzler\images\false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()    
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)
        
        
        
        
        
 