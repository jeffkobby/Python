from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from json.decoder import JSONDecodeError

white = "white"
filename = "data.json"


def write_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Add an encryption feature to the program

# ---------------------------- SEARCH ------------------------------- #
def search():
    user_search = website_entry.get()
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found",
                            message="File does not exist. Please save credentials to create file")
    except JSONDecodeError:
        messagebox.showinfo(title="Empty File", message="There is no data in file")
    else:
        if user_search in data:
            email = data[user_search]['email']
            password = data[user_search]['password']
            messagebox.showinfo(title=f"{user_search} credentials",
                                message=f"Username/Email: {email} \n"
                                        f"Password: {password}")
            pyperclip.copy(password)

        else:
            messagebox.showinfo(title=f"Logins not found",
                                message=f"Your credentials for this site does not exist")
    finally:
        website_entry.delete(0, 'end')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = random.randint(8, 10)
    number_of_numbers = random.randint(2, 4)
    number_of_symbols = random.randint(2, 4)

    random_letters = [letter for letter in random.sample(letters, number_of_letters)]
    random_numbers = [number for number in random.sample(numbers, number_of_numbers)]
    random_symbols = [symbol for symbol in random.sample(symbols, number_of_symbols)]

    password_letters = "".join(random_letters)
    password_numbers = "".join(random_numbers)
    password_symbols = "".join(random_symbols)

    string = password_letters + password_numbers + password_symbols

    password = "".join(random.sample(string, len(string)))
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website != "" and password != "":
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Do you want to save\n Username: {email}\n Password: {password}")

        # is_ok returns True is user clicks "Okay"
        if is_ok:
            try:
                with open(filename, 'r') as file:
                    # read file
                    data = json.load(file)
            except FileNotFoundError:
                # exception to handle missing file or create new file
                write_to_file(filename, new_data)
            except JSONDecodeError:
                # exception to write data into file if file is empty
                write_to_file(filename, new_data)
            else:
                # update content of the file
                data.update(new_data)
                write_to_file(filename, data)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                messagebox.showinfo(title="Success", message="Password saved successfully and copied to clipboard")

    else:
        messagebox.showerror(title="Empty Fields ❌", message="Fields cannot be empty")


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# canvas
canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# labels and entries
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(END, "test@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky="EW")

add_password_btn = Button(text="Add", width=36, command=save_to_file)
add_password_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
