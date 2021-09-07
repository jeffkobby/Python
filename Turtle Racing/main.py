from turtle import Turtle, Screen
import random

# Simulate a race with python turtle graphics package

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racing 🐢🐢🐢")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []


def create_turtles():
    """"Create multiple instances of turtles"""
    color = 0
    for turtle in range(7):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("turtle")
        turtle.color(colors[color])
        color += 1
        turtles.append(turtle)


def set_positions():
    """"Place turtles in their track positions"""
    vertical_position = 150
    for turtle in turtles:
        turtle.goto(x=-240, y=vertical_position)
        vertical_position -= 50


# Ask user to bet on a color
user_bets = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? (color):").lower()

if user_bets:
    is_race_on = True
    create_turtles()
    set_positions()
else:
    is_race_on = False


while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bets:
                print(f"the {winning_color} turtle won")
                is_race_on = False
            else:
                print(f"You lost! The {winning_color} turtle won the race")
                is_race_on = False


screen.screensize()
screen.exitonclick()
