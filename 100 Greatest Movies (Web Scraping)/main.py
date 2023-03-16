# install the following modules
import requests
from bs4 import BeautifulSoup
import lxml

# target URL
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# file to store scrapped data
filename = "movies.txt"

# load the webpage as a text file
response = requests.get(url=URL)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

# Get the name of the movies in the h3 tags and reverse the arrangement
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

# write the file names of the scrapped data into a text file
with open(filename, "w", encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")
