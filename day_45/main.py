# from os import name
from bs4 import BeautifulSoup
import bs4
import requests
from requests.api import head

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text
# print(response.text)

soup = bs4.BeautifulSoup(yc_webpage, "html.parser")

all_anchor_tags = soup.find_all("a")

article_tag = soup.find(name = "a", class_="storylink")
# print(headlines.text)
article_text = article_tag.text
article_link = article_tag.get("href")
article_upvote = soup.find(name = "span", class_="score")

print(article_text)
print(article_link)
print(article_upvote)