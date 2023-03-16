from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(executable_path=CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.browser = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """"This function scrapes upload and downlaod speeds from the website"""
        self.browser.get(url="https://www.speedtest.net")
        sleep(10)
        go_btn = self.browser.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                              '2]/div[3]/div[1]/a')
        go_btn.click()

        sleep(60)
        self.down = float(self.browser.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                     '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                     '1]/div[2]/div/div[2]/span').text)
        self.up = float(self.browser.find_element(by=By.XPATH, value='//*[@id="container"]/div/div['
                                                                       '3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                                                       '3]/div/div/div[2]/div[1]/div[3]/div/div['
                                                                       '2]/span').text)

    def tweet_at_provider(self):
        """"Login and tweet function"""
        self.browser.get(url="https://twitter.com/")
        sleep(3)
        login_btn = self.browser.find_element(by=By.XPATH,
                                              value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                    '1]/div/div[3]/div[5]/a/div')
        login_btn.click()
        sleep(3)

        username = self.browser.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                                '5]/label/div/div[2]/div/input')
        username.send_keys("nanaraw_")
        username.send_keys(Keys.ENTER)
        sleep(1)
        password = self.browser.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                                '3]/div/label/div/div[2]/div[1]/input')
        password.send_keys('@Kobby766')
        password.send_keys(Keys.ENTER)
        sleep(10)

        compose_tweet = self.browser.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                     '2]/main/div/div/div/div/div/div[2]/div/div['
                                                                     '2]/div[1]/div/div/div/div[2]/div['
                                                                     '1]/div/div/div/div/div/div/div/div/div/label'
                                                                     '/div[1]/div/div/div/div/div[2]/div/div/div/div')
        compose_tweet.send_keys(f"Upload speed: {self.up}MBPS\nDownload speed: {self.down}MBPS")

        tweet_btn = self.browser.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                 '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                                 '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()
