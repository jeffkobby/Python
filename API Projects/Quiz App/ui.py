from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.current_score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # labels
        self.score_label = Label(text=f"Score: {self.current_score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some text here",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # images
        self.true_btn_image = PhotoImage(file="images/true.png")
        self.false_btn_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_btn_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_btn_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

    def get_next_question(self):
        self.quiz.next_question()



        self.window.mainloop()
