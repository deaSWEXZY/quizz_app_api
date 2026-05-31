import tkinter as tk
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Math Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # ---- SCORE LABEL ----
        self.score_label = tk.Label(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # ---- CANVAS ----
        self.canvas = tk.Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, font=FONT, width=280)

        # ---- BUTTONS ----
        right_btn_image = tk.PhotoImage(file="images/true.png")
        wrong_btn_image = tk.PhotoImage(file="images/false.png")

        self.true = tk.Button(image=right_btn_image, highlightthickness=0, command=self.true_pressed)
        self.true.grid(row=2, column=0, padx=20, pady=20)
        self.false = tk.Button(image=wrong_btn_image, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            summary = messagebox.showinfo(title="Summary", message=f"You've reached to the end\nYour results.\nGuessed: {self.quiz.score}/10 ")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
