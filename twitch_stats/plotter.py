import sys
import plotly as py
import plotly.graph_objs as go
from datetime import datetime

def remove_underscores(str):
	return str.replace("_", " ")


games = sys.argv[1:]
data = []
for game in games:
	file = game + ".txt"
	times = []
	viewers = []
	with open(file, "r+") as f:
		lines = f.readlines()

	for i in lines:
		split_string = i.split(",")
		split_string[0] = split_string[0].strip()
		date = datetime.fromtimestamp(float(split_string[0]))
		times.append(date)
		viewers.append(split_string[1].strip())
	
	# Create a trace
	trace = go.Scatter(
		x = times,
		y = viewers,
		name = remove_underscores(game)
	)
	data.append(trace)
layout = go.Layout(title="Twitch viewers by game",
	xaxis=dict(title="Time"),
	yaxis=dict(title="Viewers"))
figure = go.Figure(data = data, layout=layout)
py.offline.plot(figure, filename="statistics.html")

