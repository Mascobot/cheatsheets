import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)#This line to to pint in Jupyter Notebook the map

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['text1', 'text2', 'text3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title'})
#This is the Data input to plot the map. The inputs are locations as list (which can come from a pandas DataFrame), locationmode which is a fixed string from plotly, colorscale which is a fixed string from plotly, text which is a list of the text ovelayed on the map states, z which is the numbers overleayed on the map, and the title on the color bar


layout = dict(geo={'scope': 'usa'})#This will define the layout of the map


choromap = go.Figure(data=[data], layout=layout)#go.Figure creates the map in the variable choromap


iplot(choromap)#This plots it in the Jupter Notebook

plot(choromap)#This plots it in a new HTML window

#### Check the Jupyer Notebook file for more details!!!
