from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

mov_webpage = response.text
# print(response.text)

soup = BeautifulSoup(mov_webpage, "html.parser")

# print(soup)

movie_names = soup.find_all(name="h3")

print(movie_names)