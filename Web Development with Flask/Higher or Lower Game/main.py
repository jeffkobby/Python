from flask import Flask, render_template
import random

app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route('/')
def index():
    return "<h1>Guess a number between 0 and 9\"" \
           "<div><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></div>"

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return "<h1>Too high. Try again\"" \
               "<div><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></div>"

    if guess < random_number:
        return "<h1>Too low. Try again\"" \
               "<div><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></div>"

    if guess == random_number:
        return "<h1>Correct!!!\"" \
               "<div><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></div>"


if __name__ == "__main__":
    app.run(debug=True)