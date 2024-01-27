import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.io
import seaborn as sns
from plotly import __version__
import cufflinks as cf
import chart_studio
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# init_notebook_mode(connected= True)
print(__version__)
plotly.io.renderers.default = 'browser'
# df1 = pd.read_csv(r'C:\Users\dohd\Downloads\df1', index_col= 0)
# df2 = pd.read_csv(r'C:\Users\dohd\Downloads\df2')
# # histogram = df1['A'].hist()
# agraph = df1['A'].plot.hist() #a general ray to call a plot type from a seaborn
# #dataframe or dataframe column
# areaplot = df2.plot.area()
# df1.plot.line()
# df2.plot.bar()
# plt.show()

#PLOTLY AND CUFFLINKS!!!!
cf.go_offline()
df = pd.DataFrame(np.random.randn(100,4), columns= ['A', 'B', 'C', 'D'])
# print(df.head())
# df2 = pd.DataFrame({'Category': 'A B C'.split(), 'Values': [32,43,50]})
# print(df2)
df.iplot()
plt.show()