import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100"

URL = f'{URL}/{date}'

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')

song_titles = [song.getText().strip() for song in songs if str(song)]


print(song_titles)
