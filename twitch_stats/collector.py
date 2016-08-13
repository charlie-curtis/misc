import re
from bs4 import BeautifulSoup as bs
from urllib import request
#url = "https://www.google.com"
#url = "https://www.twitch.tv/directory"
url = "https://www.twitch.tv/"
response = request.urlopen(url)
if response.getcode() != 200:
  print("unexpected response status")
  exit(1)
html = response.read()
soup = bs(html, 'html.parser')
f = open('data.txt', 'r+');

game_objs = soup.find_all("p", class_="title")
for game_obj in game_objs:
  viewers_obj= game_obj.find_next_sibling("p", class_="info")
  game = game_obj.string.strip()
  viewers = viewers_obj.string
  print(viewers);
  viewers = viewers.replace("viewers", "").strip()
  print(viewers);
  f.write(game + ", " + viewers + "\r\n")
