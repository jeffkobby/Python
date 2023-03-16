from twilio.rest import Client
import smtplib

TWILIO_ACCOUNT_SID = "AC3710e934e179ccba277bc5f83daa1d94"
TWILIO_AUTH_TOKEN = "2f5334670a6a6a19d643ee55a6503cac"
from_email = "jeffreydevelops@gmail.com"
p_word = "@Kobby766!"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message_body):
        message = self.client.messages.create(to="+233505043400", from_="+17755228278", body=message_body)
        print(message.sid)

    def send_email(self, email, message, google_flights_link):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=from_email, password=p_word)
        connection.sendmail(from_addr=from_email, to_addrs=email, msg=f"Subject:Cheap Flights Deals!\n\n{message}\n{google_flights_link}".encode("utf-8"))

