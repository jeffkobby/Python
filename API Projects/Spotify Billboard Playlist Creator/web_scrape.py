import requests
from bs4 import BeautifulSoup
import datetime
import lxml


class GetSongs:
    def __init__(self, date=datetime.datetime.now().strftime("%Y-%m-%d")):
        self.date = date
        self.song_list = []
        self.artiste_list = []
        self.url = f"https://www.billboard.com/charts/hot-100/{self.date}"

    def get_hot_100(self):
        """"This function scrape song titles from the BIllboard Hot 100 webpage"""
        response = requests.get(url=self.url)
        webpage = response.text
        soup = BeautifulSoup(webpage, "lxml")
        self.song_list = [song.getText().strip() for song in
                          soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")]

        self.artiste_list = [artiste.getText().strip() for artiste in
                             soup.find_all(name="span", class_="a-no-trucate")]
        song_dict = dict(zip(self.song_list, self.artiste_list))

        return song_dict