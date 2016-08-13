#!/usr/local/bin/python3
import re
import time 
import os
from bs4 import BeautifulSoup as bs
from urllib import request
dir = os.path.dirname(os.path.realpath(__file__))
print(dir)
url = "https://www.twitch.tv/"
response = request.urlopen(url)
monitored_games = ["StarCraft II", "Counter-Strike: Global Offensive", "Overwatch", "Dota 2", "League of Legends"]
if response.getcode() != 200:
	print("unexpected response status")
	exit(1)
html = response.read()
soup = bs(html, 'html.parser')
#find all the game titles
game_objs = soup.find_all("p", class_="title")
for game_obj in game_objs:
	viewers_obj= game_obj.find_next_sibling("p", class_="info")
	game = game_obj.string.strip()
	for looking_for in monitored_games: 
		if game == looking_for:
			file = dir + "/" + looking_for.replace(" ", "_") + ".txt"
			with open(file, 'a+') as f:
				print("found " + looking_for)
				viewers = viewers_obj.string.replace(",", "")
				viewers = viewers.replace("viewers", "").strip()
				current_time = int(time.time())
				f.write(str(current_time) + ", " + viewers + "\r\n")
