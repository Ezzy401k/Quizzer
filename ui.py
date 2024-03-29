from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, width=250, text="",
                                                font=("Arial", 20, "italic"))
        image = PhotoImage(file="images/true.png")
        self.get_next_question()

        self.true = Button(image=image, highlightthickness=0, command=self.true)
        self.true.grid(column=0, row=2)
        image2 = PhotoImage(file="images/false.png")
        self.false = Button(image=image2, highlightthickness=0, command=self.false)
        self.false.grid(column=1, row=2)
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=q_text)

        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz.{self.quiz.score}/10")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true(self):
        val = "True"
        is_right = self.quiz.check_answer(val)
        self.feedback(is_right)

    def false(self):
        val = "False"
        is_right = self.quiz.check_answer(val)
        self.feedback(is_right)

    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)