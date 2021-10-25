import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "ea9a2e9bb5b94acfa467f778f64d1cac"
Secret_Key = "7162a84b02134dedb86c56c1ded17fca"
Redirect_URI = "http://example.com/"


# Scraping Billboard top 100 songs
print("Welcome to Musical time machine")
time_travel_to = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + time_travel_to)
songs_res = response.text
soup = BeautifulSoup(songs_res, "html.parser")
all_heading_tags = soup.find_all(name="span", class_="chart-element__information__song")
all_songs = [tag.getText() for tag in all_heading_tags]
# print(all_songs)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=Client_ID,
        client_secret=Secret_Key,
        redirect_uri=Redirect_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = time_travel_to.split("-")[0]
for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new playlist
Playlist_ID = time_travel_to+" Billboard 100"
new_playlist = sp.user_playlist_create(user=user_id, name=Playlist_ID,
                                       description="Top 100 songs", public=False)
# for uri in song_uris:
add_songs = sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)


