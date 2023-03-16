from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pprint import pp

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(executable_path=CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=service)

# time
timeout = time.time() + 5
five_minutes = time.time() + 60*5

print(timeout)
print(five_minutes)

browser.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie_btn = browser.find_element(by=By.ID, value="cookie")

store_items = browser.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store_items]




isClicking = True
while isClicking:
    cookie_btn.click()

    # after every five seconds
    if time.time() > timeout:

        # get all upgrades
        upgrade_products = browser.find_elements_by_css_selector(css_selector="#store b")
        prices = []

        # convert upgrade text into int variables
        for price in upgrade_products:
            try:
                amount = int(price.text.split("-")[1].strip().replace(",", ""))
                prices.append(amount)
            except IndexError:
                pass

        # create dictionary of store items and prices
        upgrades = dict(zip(prices, item_ids))

        # get current cookie count
        cookie_count_element = browser.find_element(by=By.ID, value="money").text
        if "," in cookie_count_element:
            cookie_count_element = cookie_count_element.replace(",", "")
        cookie_count = int(cookie_count_element)

        # find affordable upgrades
        affordable_upgrades = {}
        for cost, id in upgrades.items():
            if cookie_count > cost:
                affordable_upgrades['cost'] = id

        # purchase most expensive upgrade
        try:
            most_expensive_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[most_expensive_upgrade]
            to_purchase = browser.find_element(by=By.ID, value=to_purchase_id)
            to_purchase.click()
        except ValueError:
            continue

        # Add another five seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        # if time.time() > five_minutes:
        #     cookie_per_s = browser.find_element_by_id("cps").text
        #     print(cookie_per_s)










# browser.quit()




