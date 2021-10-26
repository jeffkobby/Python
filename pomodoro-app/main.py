from tkinter import *
from functionalities import Functionalities


class UserInterFace(Functionalities):
    def __init__(self):
        super().__init__()

        # fonts and colors
        self.PINK = "#e2979c"
        self.RED = "#e7305b"
        self.GREEN = "#9bdeac"
        self.YELLOW = "#f7f5dd"
        self.FONT_NAME = "Courier"

        # main window
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=self.YELLOW)

        # timer label
        self.timer_label = Label(text="Timer")
        self.timer_label.config(fg=self.GREEN, bg=self.YELLOW, font=(self.FONT_NAME, 30, "bold"))
        self.timer_label.grid(row=0, column=1)

        # create the canvas for image
        self.canvas = Canvas(width=200, height=224, bg=self.YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(103, 130, text="00:00", fill="white", font=(self.FONT_NAME, 35,
                                                                                              "bold"))
        self.canvas.grid(row=1, column=1)

        # start button
        self.start_btn = Button(text="Start", highlightthickness=0, command=super().start_timer)
        self.start_btn.grid(row=2, column=0)

        # reset button
        self.reset_btn = Button(text="Reset", highlightthickness=0, command=super().reset_timer)
        self.reset_btn.grid(row=2, column=2)

        # checkmark label
        self.check_label = Label()
        self.check_label.config(fg=self.GREEN, bg=self.YELLOW, font=(self.FONT_NAME, 15, "bold"))
        self.check_label.grid(row=3, column=1)


main_window = UserInterFace()

main_window.window.mainloop()
