from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'http://www.imdb.com/chart/top'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
films = soup.find_all("td", class_="titleColumn")
notes = soup.find_all("td", class_="imdbRating")

movie_list = []

for index in range(0, len(films)):
    film_text = films[index].get_text()
    notes_text = notes[index].get_text()
    film = (' '.join(film_text.split()).replace('.', ''))
    film_title = film[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', film_text).group(1)
    data = {
            "film_title": film_title,
            "note": notes_text,
            "year": year,
            }
    movie_list.append(data)

for film in movie_list:
    print(film['film_title'], '(' + film['year'] + ')', film['note'])
