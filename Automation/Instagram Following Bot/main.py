from insta_follower import InstaFollower

SIMILAR_ACCOUNT = "leomessi"
USERNAME = "jeffreydevelops@gmail.com"
PASSWORD = "Kobby766"

insta_bot = InstaFollower()
insta_bot.login(USERNAME, PASSWORD)
insta_bot.find_followers(SIMILAR_ACCOUNT)
insta_bot.follow()

