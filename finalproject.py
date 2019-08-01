# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:38:43 2019

@author: STEM
"""

import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go
#We read the data into a dataset or data frame called df
wceodf=pd.read_excel("GISdata.xlsx",sheet_name=("womenCEOs"))
wceodf
#We use the bar graph option of the graph_objs function from the plotly library
wceograph=go.Bar(x=wceodf["Year"],y=wceodf["CEOs"],
                  marker={"color":wceodf["CEOs"],"colorscale":"magenta"})

title = go.Layout(title="Percent of Female CEOs by Year",
                  xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Year")),
                  yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage")))

fig=go.Figure(data=[wceograph],layout=title)
plot(fig)

#We use Figure option of the graph_obj function from the plotly library 
#We call the plot function from the plotly.offline library