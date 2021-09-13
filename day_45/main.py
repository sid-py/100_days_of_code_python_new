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

article_tags = soup.find_all(name="a", class_= "storylink")
article_upvote = soup.find_all(name = "span", class_="score")
for article_headline in article_tags:
    article_text = article_headline.text
    article_link = article_headline.get("href")
    print(article_headline.text)
    print(article_link)
for vote_line in article_upvote:
    votes = vote_line.text
    vote = votes.split()
    vote_count = int(vote[0])
    print(vote_count)
 
