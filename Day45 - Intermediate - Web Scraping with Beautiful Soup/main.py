import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_html = response.text

bs_obj = BeautifulSoup(website_html, "html.parser")

movies_list = bs_obj.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies_list]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
