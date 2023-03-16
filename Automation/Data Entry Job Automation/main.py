import time
from pprint import pprint
from listing_info import ListingInfo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

listing_info = ListingInfo()
property_info = listing_info.get_property_info()

# start automation
GOOGLE_FORM_LINK = "https://forms.gle/QU4AUV9dhxUQMFid6"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
chrome_options = Options().add_experimental_option("detach", True)
service = Service(executable_path=CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get(url=GOOGLE_FORM_LINK)

for key, value in property_info.items():
    # for every iteration, find the following DOM Elements
    address_input = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                            '2]/div/div[1]/div/div[1]/input')
    price_input = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                          '2]/div/div[1]/div/div[1]/input')
    link_input = browser.find_element(by=By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    submit_btn = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address = value['address']
    link = value['link']
    price = value['price']

    time.sleep(3)

    # fill inputs with info
    address_input.send_keys(address)
    link_input.send_keys(link)
    price_input.send_keys(price)
    submit_btn.click()

    time.sleep(3)

    # submit another response
    another_response = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(3)

browser.quit()
