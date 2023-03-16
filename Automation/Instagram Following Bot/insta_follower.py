import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(executable_path=CHROME_DRIVER_PATH)


class InstaFollower:
    def __init__(self):
        self.browser = webdriver.Chrome(service=service)

    def login(self, u_name, p_word):
        self.browser.get(url="https://www.instagram.com/")
        time.sleep(5)

        username = self.browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(u_name)
        password = self.browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(p_word)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        not_now_btn_1 = self.browser.find_element(by=By.XPATH,
                                                  value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn_1.click()
        time.sleep(10)

    def find_followers(self, target_acc):
        self.browser.get(url=f"https://www.instagram.com/{target_acc}")
        time.sleep(5)
        target_acc_followers = self.browser.find_element(by=By.XPATH,
                                                         value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        target_acc_followers.click()
        time.sleep(3)
        scroll = self.browser.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')

        for i in range(10):
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)

    def follow(self):
        all_buttons = self.browser.find_elements(by=By.CLASS_NAME, value="sqdOP")
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


#         def follow(self):
#
#         people_to_follow = []
#         offset_height_all_followers = self.browser.execute_script(
#             'return document.querySelector(".isgrP").offsetHeight;')
#         total_height_all_followers = self.browser.execute_script(
#             'return document.querySelector(".isgrP").scrollHeight;')
#         new_height = offset_height_all_followers + 5
#
#         while new_height < total_height_all_followers:
#             follow = self.browser.find_elements_by_css_selector("button.sqdOP")
#             people_to_follow.append(follow)
#
#             if total_height_all_followers < 1000:  # this number can be changed so it will scroll more and collect more followers
#                 people_to_follow_extracted = people_to_follow[0]
#                 time.sleep(2)
#                 for follower in people_to_follow_extracted:
#                     try:
#                         time.sleep(2)
#                         follower.click()
#                         time.sleep(3)
#                     except ElementClickInterceptedException:
#                         pass
#             self.browser.execute_script(f'document.querySelector(".isgrP").scrollTo(0, {new_height})')
#             new_height += 5
#             total_height_all_followers = self.browser.execute_script(
#                 'return document.querySelector(".isgrP").scrollHeight;')
#             if total_height_all_followers > 1000:  # this number can be changed so it will scroll more and collect more followers
#                 break;
#         self.browser.quit()
