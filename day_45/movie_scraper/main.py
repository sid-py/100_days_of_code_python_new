from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

mov_webpage = response.text
# print(response.text)

soup = BeautifulSoup(mov_webpage, "html.parser")

# print(soup.prettify)

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
print(all_movies)

