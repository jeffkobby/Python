import pandas as pd
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox


class BirthdayManager:
    def __init__(self):
        # window
        self.window = Tk()
        self.window.title("Birthday Manager")
        self.window.config(padx=50, pady=20)

        # labels and entries
        self.name_label = Label(text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = Entry(width=30)
        self.name_entry.focus()
        self.name_entry.grid(row=0, column=1, stick="EW")

        self.email_label = Label(text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_entry = Entry(width=30)
        self.email_entry.focus()
        self.email_entry.grid(row=1, column=1, stick="EW")

        self.date_label = Label(text="Date:")
        self.date_label.grid(row=3, column=0)
        self.calendar = Calendar(self.window, date_pattern="y-m-d")
        self.calendar.grid(row=3, column=1, stick="EW")

        # button
        self.add_btn = Button(text="Add Entry", width=15, command=self.add_entry)
        self.add_btn.grid(row=4, column=2)

        # variables
        self.FILENAME = "C:/Users/jeffk/PycharmProjects/Birthday Wisher (Day 32) start/birthdays.csv"
        self.date = ""
        self.dict = {
            "name": "",
            "email": "",
            "year": "",
            "month": "",
            "day": ""
        }

    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)

    def add_entry(self):
        self.date = self.split_date(self.calendar.get_date())
        self.dict['name'] = self.name_entry.get()
        self.dict['email'] = self.email_entry.get()
        self.dict['year'] = self.date[0]
        self.dict['month'] = self.date[1]
        self.dict['day'] = self.date[2]
        messagebox.showinfo(title="", message="Entry added")
        self.create_csv()
        self.clear_entries()

    def split_date(self, date):
        date = self.calendar.get_date()
        date_list = date.split("-")

        return date_list

    def create_csv(self):
        try:
            dataframe = pd.read_csv(self.FILENAME)
        except FileNotFoundError:
            dataframe = pd.DataFrame(self.dict, index=[0])
            dataframe.to_csv(self.FILENAME, index=False)
        else:
            self.date = self.split_date(self.calendar.get_date())
            dataframe_dict = dataframe.to_dict(orient="list")
            dataframe_dict["name"] = self.name_entry.get()
            dataframe_dict["email"] = self.email_entry.get()
            dataframe_dict["year"] = self.date[0]
            dataframe_dict["month"] = self.date[1]
            dataframe_dict["day"] = self.date[2]
            dataframe = dataframe.append(dataframe_dict, ignore_index=True)
            dataframe.to_csv(self.FILENAME, index=False)


manager = BirthdayManager()
manager.window.mainloop()