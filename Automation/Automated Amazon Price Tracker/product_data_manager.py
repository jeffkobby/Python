import requests
from bs4 import BeautifulSoup
import lxml

class ProductData:
    # This product handles necessary product data from Amazon
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
            "Accept-Language": "en-US,en;q=0.5"
        }
        self.EXCHANGE_RATES_API_ENDPOINT = "http://api.exchangeratesapi.io/v1/"
        self.EXCHANGE_RATES_API_KEY = "3984b152b379ea53cc3bff3e12d69a02"

    def get_product_data(self):
        response = requests.get(url="https://www.amazon.com/RESPAWN-110-Racing-Style-Gaming-Chair/dp/B076HTJRMZ/ref=sr_1_3?keywords=gaming+chairs&pd_rd_r=5b8a72b1-1bd3-437a-9555-51e9d9c4cfe7&pd_rd_w=EfvQ0&pd_rd_wg=fnM03&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=N2PAKA2A49K8PGPJ4FPE&qid=1645132064&sr=8-3",
                                headers=self.header)
        response.raise_for_status()
        result = response.text

        try:
            soup = BeautifulSoup(result, "lxml")
            product_name = soup.find(name="span", id="productTitle").get_text().strip()
            product_price = float(soup.find(name="span", id="priceblock_ourprice").get_text().split('$')[1])
            product_image_tage = soup.find(name="img", id="landingImage")
            product_image = product_image_tage['src']

            product_data = {
                "itemName": product_name,
                "price": product_price,
                "image": product_image,
                "priceInCedis": {round(self.get_exchange_rate() * product_price, 2)}
            }

            return product_data

        except AttributeError:
            soup = BeautifulSoup(result, "lxml")
            product_name = soup.find(name="span", id="productTitle").get_text().strip()
            product_price = float(soup.find(name="span", class_="a-offscreen").get_text().split('$')[1])
            product_image_tage = soup.find(name="img", id="landingImage")
            product_image = product_image_tage['src']

            product_data = {
                "itemName": product_name,
                "price": f"${product_price}",
                "image": product_image,
                "priceInCedis": f"₵{round(self.get_exchange_rate() * product_price, 2)}"
            }

            return product_data

    def get_exchange_rate(self):

        params = {
            "access_key": self.EXCHANGE_RATES_API_KEY,
            "base": "EUR"
        }
        response = requests.get(url=f"{self.EXCHANGE_RATES_API_ENDPOINT}latest", params=params)
        response.raise_for_status()
        result = response.json()
        rate_in_dollars = result['rates']['USD']
        rate_in_cedi = result['rates']['GHS']
        usd_to_ghs_rate = rate_in_cedi / rate_in_dollars

        return usd_to_ghs_rate

product = ProductData()
product.get_exchange_rate()
