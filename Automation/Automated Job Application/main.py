from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# functions
def login(email, password):
    username_input = browser.find_element(by=By.ID, value="username")
    username_input.send_keys(email)

    password_input = browser.find_element(by=By.ID, value="password")
    password_input.send_keys(password)

    login_btn = browser.find_element(by=By.CLASS_NAME, value="btn__primary--large")
    login_btn.click()


def save_job_listing():
    save_button = browser.find_element(by=By.CLASS_NAME, value="jobs-save-button")
    save_button.click()


def save_multiple_jobs():
    search_results = browser.find_elements(by=By.ID, value="jobs-search-results__list-item")
    save_buttons = browser.find_elements(by=By.CLASS_NAME, value="jobs-save-button")

    for search_result in search_results:
        search_result.click()



email = "jeffreydevelops@gmail.com"
password = "Kobby766"

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get(url="https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105769538&keywords=python%20developer&location=Ghana")

try:
    sign_in = browser.find_element(by=By.LINK_TEXT, value="Sign in")
    sign_in.click()

    # wait for page to load
    time.sleep(3)
except Exception as error:
    print(error)
else:
    login(email, password)
    time.sleep(10)
    save_multiple_jobs()



