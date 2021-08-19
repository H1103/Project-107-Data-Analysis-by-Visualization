import pandas as pd 
import csv
import plotly.express as px 
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
# as_index = False means you indicate to groupby() that you don't want to set the column ID as the index
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")
fig.show()