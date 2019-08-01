# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:07:40 2019

@author: STEM
"""
import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go
womendf=pd.read_excel("GISdata.xlsx",sheet_name=("womenOccupation"))
womendf


title = go.Layout(title="% of Women by Occupation")
womengraph=go.Bar(x=womendf["Occupation"],y=womendf["Women"])
fig=go.Figure(data=[womengraph],layout=title)
plot(fig)
