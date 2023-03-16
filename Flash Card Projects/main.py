from tkinter import *
import pandas as pd
from pandas.errors import EmptyDataError
import random

word_file = pd.read_csv("data/french_words.csv")
word_list = word_file.to_dict(orient="records")

card_choice = {}


BACKGROUND_COLOR = "#B1DDC6"


def get_french_word(choice):
    """"A function to get values of the 'French' key in word_file_dict'"""
    canvas.itemconfig(language, text="French", fill="black")
    french_word = choice['French']
    canvas.itemconfig(word, text=french_word, fill="black")


def next_card():
    """"Function to select a new word from the word_file_dict file"""
    try:
        global card_choice, timer
        window.after_cancel(timer)
        canvas.itemconfig(canvas_image, image=card_front)
        words_to_learn = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        card_choice = random.choice(word_list)
        get_french_word(card_choice)
    except EmptyDataError:
        card_choice = random.choice(word_list)
        get_french_word(card_choice)
    else:
        words_to_learn_list = words_to_learn.to_dict(orient="records")
        card_choice = random.choice(words_to_learn_list)
    finally:
        get_french_word(card_choice)
        timer = window.after(3000, func=flip_card)


def is_known():
    global card_choice
    word_list.remove(card_choice)
    new_data = pd.DataFrame(word_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



def flip_card():
    """A function to 'flip' or change the image and text of a card"""
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=card_choice["English"], fill="white")


# Window setup
window = Tk()
window.title("Flash Cards Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# timer function
timer = window.after(3000, func=flip_card)

# setup card images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

# setup the canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(405, 270, image=card_front)

# canvas text
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))

canvas.grid(row=0, column=0, columnspan=2)


# setup buttons
red_button_image = PhotoImage(file="images/wrong.png")
green_button_image = PhotoImage(file="images/right.png")

red_button = Button(image=red_button_image, highlightthickness=0, command=next_card)
red_button.grid(row=1, column=0)

green_button = Button(image=green_button_image, highlightthickness=0, command=is_known)
green_button.grid(row=1, column=1)


next_card()
window.mainloop()

