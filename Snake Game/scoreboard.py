from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILENAME = 'data.txt'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def get_high_score(self):
        with open(FILENAME) as file:
            content = file.read()
        return content

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILENAME, mode='w') as file:
                content = file.write(str(self.high_score))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
