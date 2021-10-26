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
# time_travel_to = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.google.com/search?q=Top+100+Ilayaraja+songs+&biw=1280&bih=577&sxsrf="
                        "AOaemvICL8veOzhtiICdosvkCYP8-lbHsQ%3A1635165522504&ei=UqV2YdycHoelytMP_7aL8A0&ved"
                        "=0ahUKEwjcjfigyuXzAhWHknIEHX_bAt4Q4dUDCA4&uact=5&oq=Top+100+Ilayaraja+songs+&gs_lcp="
                        "Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsANKBAhB"
                        "GABQrjJYrjJgjzdoAnACeACAATeIATeSAQExmAEAoAEByAEIwAEB&sclient=gws-wiz")
songs_res = response.text
soup = BeautifulSoup(songs_res, "html.parser")
# print(soup.prettify())
all_heading_tags = soup.find_all(name="div", class_="BNeawe deIvCb AP7Wnd")
all_songs = [tag.getText() for tag in all_heading_tags]
all_songs = all_songs[1:50]


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
for song in all_songs:
    result = sp.search(q=f"track:{song}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new playlist
Playlist_ID = "Best Ilayaraja songs"
new_playlist = sp.user_playlist_create(user=user_id, name=Playlist_ID,
                                       description="Best Ilayaraja songs playlist created by lisi in python", public=False)
# for uri in song_uris:
add_songs = sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)


