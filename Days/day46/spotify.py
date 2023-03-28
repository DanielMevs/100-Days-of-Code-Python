from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100"

URL = f'{URL}/{date}'

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')

song_titles = [song.getText().strip() for song in songs if str(song)]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="<YOUR UNIQUE CLIENT ID>",
        client_secret="<YOUR UNIQUE CLIENT SECRET>",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)