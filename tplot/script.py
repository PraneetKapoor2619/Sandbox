#ternary plotting script
import pandas as pd
import plotly.express as px
dataframe1 = pd.read_excel("MIMA.xlsx",
sheet_name="micro bc tp",
header=0,
index_col=False,
keep_default_na=True
)
print(dataframe1)
fig = px.scatter_ternary(dataframe1, a = 'O/C', b = 'H/C', c = 'N/C', hover_name='Name', color='Name')
fig.show() 