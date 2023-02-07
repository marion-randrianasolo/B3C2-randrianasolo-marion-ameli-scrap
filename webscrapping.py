from bs4 import BeautifulSoup
import requests

url = 'http://www.imdb.com/chart/top'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
