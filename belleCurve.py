import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv("phone.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Samsung"],show_hist=False)
fig.show()