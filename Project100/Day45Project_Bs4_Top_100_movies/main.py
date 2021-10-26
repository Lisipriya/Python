import requests
from bs4 import BeautifulSoup

response = requests.get("http://web.archive.org/web/20200515133712/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")
movie_res = response.text

soup = BeautifulSoup(movie_res, "html.parser")
# print(soup.prettify())
all_heading_tags = soup.find_all(name="h3", class_="title")

all_movies = [tag.getText() for tag in all_heading_tags]
movies_from_start = all_movies[::-1]

with open ("top_100_movies.txt", "w") as file:
    for movie in movies_from_start:

        file.write( f"{movie}\n")

