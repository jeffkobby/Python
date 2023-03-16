import smtplib

class NotificationManager:
    # This class is responsible for sending emails when there is a price drop
    def __init__(self):
        self.FROM_ADDRESS = "jeffreydevelops@gmail.com"
        self.PASSWORD = "@Kobby766!"
        self.TO_ADDRESS = "nanayawkm1634@gmail.com"
        self.location = "smtp.gmail.com"
        self.name = "Jeffrey"

    def send_message(self, cheaper_prices):
        connection = smtplib.SMTP(host=self.location, port=587)
        connection.starttls()
        connection.login(user=self.FROM_ADDRESS, password=self.PASSWORD)

        for key,value in cheaper_prices.items():
            name = value['name']
            price = value['price']
            priceInCedis = value['priceInCedis']
            image = value['image']
            connection.sendmail(from_addr=self.FROM_ADDRESS, to_addrs=self.TO_ADDRESS, msg=f"Subject: Price drop found for {name}‼‼\n\n"
                                        f"Hello {self.name}, we have detected a price drop for the item: {name}\n"
                                        f"Current price is ${price} which directly converts GHS{priceInCedis}"
                                        f"Below is an of of {name}\n"
                                        f"{image}".encode("utf-8"))

