from bs4 import BeautifulSoup
import requests

response = requests.get("https://stackoverflow.com/questions/56478652/scraping-text-in-h3-and-p-tags-using-beautifulsoup-python")

mov_webpage = response.text
# print(response.text)

soup = BeautifulSoup(mov_webpage, "html.parser")

# print(soup.prettify)

all_movies = soup.find(name="h3", class_="flex--item fs-title")
print(all_movies.text)

