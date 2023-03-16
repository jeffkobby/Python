from turtle import Turtle, Screen
import pandas as pd


def get_mouse_click_coor(x,y):
    """"A function that outputs coordinates on the turtle screen"""
    print(x, y)


image = "blank_states_img.gif"

# turtle and screen objects
turtle = Turtle()
screen = Screen()

screen.title("US States Game")

screen.addshape(image)
turtle.shape(image)

# pandas object
data = pd.read_csv("50_states.csv")
states = data['state'].to_list()
correct_guesses = []
score = 0


def check_state(user_answer):
    """"If user guesses a state correctly, draw the state in its coordinates"""
    if user_answer in states:
        correct_guesses.append(user_answer)
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)
        global score
        score += 1
    else:
        print("false")


is_on = True
while is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50", prompt="Another state:").title()

    if answer_state == "Exit":
        screen.bye()

    check_state(answer_state)

# states to learn



# listen to mouse clicks
# screen.onscreenclick(get_mouse_click_coor)

# keeps screen running
screen.mainloop()
