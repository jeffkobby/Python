from web_scrape import GetSongs
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pp

# inputs
user_date = input("Enter a date in the format YYYY-MM-DD: \n")

# class objects
songs = GetSongs(user_date)

# variables
scope = "playlist-modify-private"
redirect_uri = "https://example.com"
song_dict = songs.get_hot_100()
year = user_date.split('-')[0]
song_uri_list = []

# Implements Authorization Code Flow for Spotify’s OAuth implementation
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="26b08d97c2444d06a71d53f5008faad4",
        client_secret="91d54d904c744c2d9cf993cf43396f1b",
        redirect_uri=redirect_uri,
        cache_path="token.txt",
        scope=scope,
        show_dialog="True",
    )
)

# get the spotify user id
user_id = spotify.current_user()['id']

# search for the uri of each song and store it in the "song_uri_list"
for song, artist in song_dict.items():
    results = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = results['tracks']['items'][0]['uri']
        song_uri_list.append(uri)
    except IndexError:
        print(f"{song} does not exist on Spotify. Skipped")

# create the playlist
playlist = spotify.user_playlist_create(user=user_id, public=False, name=f"{user_date} Billboard Hot 100")

# add songs to the playlist
spotify.playlist_add_items(playlist_id=playlist['id'], items=song_uri_list)
