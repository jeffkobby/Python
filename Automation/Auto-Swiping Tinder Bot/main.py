import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# FB Account Info
FB_EMAIL = "jeffreydevelops@gmail.com"
FB_PASSWORD = "AQ5leW!aKdep5xi0"

# Browser setup
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
browser = webdriver.Chrome(service=service)
url = "https://tinder.com/"
browser.get(url=url)

# Explicit Wait with Selenium
# Waits for AJAX to load DOM
try:
    login = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")))
except Exception as e:
    print(e)
else:
    # click on the login buttons and wait for popup to show
    login.click()
    time.sleep(3)
    login_with_fb = browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
    # click "log in with Facebook"
    login_with_fb.click()
    time.sleep(5)

    # get browser window ids
    windows = browser.window_handles
    main_window = windows[0]
    facebook_login_window = windows[1]

    # focus on the facebook window
    browser.switch_to.window(facebook_login_window)

    # login with facebook in facebook window
    email_input = browser.find_element(by=By.XPATH, value='//*[@id="email"]')
    email_input.send_keys(FB_EMAIL)
    password_input = browser.find_element(by=By.XPATH, value='//*[@id="pass"]')
    password_input.send_keys(FB_PASSWORD)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # focus on the main/base window after logging in
    browser.switch_to.window(main_window)

    # wait for page elements to load
    time.sleep(10)

    # dimiss requests
    browser.find_element(by=By.XPATH,
                         value='//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]').click()
    browser.find_element(by=By.XPATH,
                         value='//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[2]').click()

    # wait for tinder profiles to show
    time.sleep(10)

    # get the like button
    like_btn = browser.find_element(by=By.XPATH, value='//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div['
                                                       '1]/div/div/div[4]/div/div[4]/button')

    count = 50
    while count != 0:
        try:
            like_btn.click()
        except ElementClickInterceptedException:
            browser.find_element_by_css_selector(".itsAMatch a").click()
        else:
            pass
        finally:
            time.sleep(3)
            count -= 1
