from bs4 import BeautifulSoup




with open(r"day_45\website.html") as file:
    contents = file.read()
    

soup = BeautifulSoup(contents)
print(soup)    