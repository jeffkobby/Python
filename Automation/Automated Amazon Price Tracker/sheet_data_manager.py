import requests
from pprint import pp

class SheetData:
    # This class handles every data that comes from our Google Sheet
    def __init__(self):
        self.url = "https://api.sheety.co/2b19ebd89a834491a7f81a5bf5f84b61/priceTracker/prices"

    def get_sheet_data(self):
        response = requests.get(url=self.url)
        result = response.json()

        return result

    def post_data(self, product):
        body = {
            "price": product
        }

        pp(body)

        response = requests.post(url=self.url, json=body)
        response.raise_for_status()


    def check_prices(self):
        # This class compares the current prices to the set prices and will return a new dictionary
        # if set conditions are true

        sheet_rows = self.get_sheet_data()['prices']
        cheaper_prices = {}

        for row in sheet_rows:
            if row['price'] < row['setPrice']:
                new_entry = {
                    "name": row['itemName'],
                    "price": row['price'],
                    "setPrice": row['setPrice'],
                    "priceInCedis": row['priceInCedis'],
                    "image": row['image']
                }
                cheaper_prices[row['id']] = new_entry
            else:
                pass

        return cheaper_prices



sheet = SheetData()
sheet.check_prices()

