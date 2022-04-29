
# WIP #

from bs4 import BeautifulSoup
import requests

# user_choice = input("What year do you want to travel to? YYYY-MM-DD \n")
# TODO! 10. Need to delete below line of code when finished, and uncomment line above
user_choice = "2005-07-09"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_choice}/")
top100_webpage = response.text

soup = BeautifulSoup(top100_webpage, "html.parser")
# TODO! 1. Need to read up on soup.select and why below line of code works.
titles = soup.select(selector="li h3", class_="c-title")
songs_list = []

# TODO! 2. Need to make this into list comprehension
for t in titles:
    text = t.getText().strip()
    songs_list.append(text)

print(songs_list)
