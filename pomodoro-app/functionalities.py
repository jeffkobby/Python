import math

# TODO: Make window appear in front of all other windows after timer runs down


class Functionalities:
    def __init__(self):

        # work time
        self.WORK_MIN = 25
        self.SHORT_BREAK_MIN = 5
        self.LONG_BREAK_MIN = 20
        self.rep_count = 0
        self.timer = None

    def start_timer(self):
        """"Call the countdown function when the user clicks on start"""
        work_seconds = self.WORK_MIN * 60
        short_break_seconds = self.SHORT_BREAK_MIN * 60
        long_break_seconds = self.LONG_BREAK_MIN * 60
        self.rep_count += 1

        # take a long break after on the eight rep
        if self.rep_count % 8 == 0:
            self.count_down(int(long_break_seconds))
            self.timer_label.config(text="Break", fg=self.RED
                                    )
        # take a short break for after every work session
        elif self.rep_count % 2 == 0:
            self.count_down(int(short_break_seconds))
            self.timer_label.config(text="Break", fg=self.PINK)

        else:
            self.count_down(work_seconds)
            self.timer_label.config(text="Work Time!", fg=self.GREEN)

    def count_down(self, count):
        """"Start countdown function"""

        # GET MINUTES AND SECONDS
        count_min = math.floor(count / 60)
        count_seconds = count % 60

        if count_seconds < 10:
            self.canvas.itemconfig(self.timer_text, text=f"{count_min}:0{count_seconds}")
        else:
            self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_seconds}")

        # call the count down function to mimic a countdown clock simulation
        if count > 0:
            # call countdown function after 1s if count != 0
            # increase rep count

            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()

            # for every two work sessions, add a check mark
            work_sessions = math.floor(self.rep_count / 2)
            marks = ""
            for item in range(work_sessions):
                marks += "✔"
            self.check_label.config(text=marks)

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.timer_label.config(text="Timer")
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.check_label.config(text="")
        self.rep_count = 0
