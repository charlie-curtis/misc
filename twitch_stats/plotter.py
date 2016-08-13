import sys
import plotly as py
import plotly.graph_objs as go
from datetime import datetime

game = sys.argv[1]
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
	print(date)
	viewers.append(split_string[1].strip())
	
print(times)
print(viewers)
# Create a trace
trace = go.Scatter(
    x = times,
    y = viewers 
)

data = [trace]

py.offline.plot(data, filename=game + ".html")

