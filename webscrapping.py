from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'http://www.imdb.com/chart/top'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
films = soup.find_all("td", class_="titleColumn")
notes = soup.find_all("td", class_="imdbRating")

