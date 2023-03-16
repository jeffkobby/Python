from bs4 import BeautifulSoup
import lxml
import requests

ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
              "%22mapBounds%22%3A%7B%22west%22%3A-122.66026534033203%2C%22east%22%3A-122.20639265966797%2C%22south%22" \
              "%3A37.618763407635534%2C%22north%22%3A37.93148879622303%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22" \
              "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22" \
              "%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B" \
              "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C" \
              "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B" \
              "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D "


class ListingInfo:
    """"This class is responsible for scraping relevant listing info from Zillow"""
    def __init__(self):
        self.property_info = {}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
            "Accept-Language": "en-US,en;q=0.5"
        }
        self.link_list = []
        self.price_list = []
        self.address_list = []

    def get_property_info(self):
        """"returns the property information as a list"""
        response = requests.get(url=ZILLOW_LINK, headers=self.headers)
        result = response.text

        soup = BeautifulSoup(result, "lxml")

        # get address
        self.address_list = [address.text for address in soup.find_all(name="address", class_="list-card-addr")]

        # get links
        card_links = soup.select(selector=".list-card-top a")
        for card_link in card_links:
            href = card_link['href']
            if "http" not in href:
                self.link_list.append(f"https://www.zillow.com/{href}")
            else:
                self.link_list.append(href)

        # get rent prices
        card_prices = soup.find_all(name="div", class_="list-card-price")
        for card_price in card_prices:
            card_price_text = card_price.text

            split_unformatted_card_price = card_price_text.split("/mo")
            split_card_price_text = split_unformatted_card_price[0]

            if "+" in split_card_price_text:
                get_price = split_card_price_text.split("+")[0]
                self.price_list.append(get_price)
            else:
                self.price_list.append(split_card_price_text)

        for listing_id in range(len(self.address_list)):
            self.property_info[listing_id] = {
                "address": self.address_list[listing_id],
                "price": self.price_list[listing_id],
                "link": self.link_list[listing_id]
            }

        return self.property_info
