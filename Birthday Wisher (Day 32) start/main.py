import smtplib
import datetime as dt
import pandas as pd
import random

filename = "birthdays.csv"


class AutomatedBirthdayWisher:
    def __init__(self):
        self.MY_EMAIL = "jeffreydevelops@gmail.com"
        self.MY_PASSWORD = "@Kobby766!"
        self.RECEIVER_EMAIL = ""
        self.FILENAME = "birthdays.csv"
        self.LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        self.random_letter = random.choice(self.LETTERS)
        self.current_date = dt.datetime.now()
        self.day = self.current_date.day
        self.month = self.current_date.month
        self.today = (self.month, self.day)

    def get_info(self):
        # read the csv file
        birthday_df = pd.read_csv(self.FILENAME)

        # use dictionary comprehension row info with (birth month, birthday) as key
        birthday_df_dict = {(row.month, row.day): row for (column, row) in birthday_df.iterrows()}

        # compare current day & month to dictionary keys
        if self.today in birthday_df_dict:
            self.RECEIVER_EMAIL = birthday_df_dict[self.today]["email"]

            with open(self.random_letter) as file:
                letter = file.read()
                new_letter = letter.replace("[NAME]", birthday_df_dict[self.today]['name'])

            self.send_email(new_letter, self.RECEIVER_EMAIL)

    def send_email(self, message, to_address):
        """Create a connection and send message to recipient"""
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.MY_EMAIL, password=self.MY_PASSWORD)
                connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=to_address,
                                    msg=f"Subject: Happy Birthday "
                                        f"\n\n {message}")
        except Exception as error:
            print(error)
        else:
            print("Email sent successfully")


automated_birthday = AutomatedBirthdayWisher()
automated_birthday.get_info()


