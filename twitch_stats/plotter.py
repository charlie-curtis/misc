import plotly as py
import plotly.graph_objs as go

# Create random data with numpy

random_x = [1,2,3,4,5];
random_y = [1,2,3,4,15];

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

py.offline.plot(data, filename='basic-line')

