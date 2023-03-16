import time

from twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWNLOAD_SPEED = 60
PROMISED_UPLOAD_SPEED = 70
TWITTER_EMAIL = "jeffreydevelops@gmail.com"
TWITTER_PASSWORD = "Kobby766"

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.up < PROMISED_UPLOAD_SPEED or bot.down < PROMISED_DOWNLOAD_SPEED:
    bot.tweet_at_provider()
    time.sleep(3)
    bot.browser.quit()

