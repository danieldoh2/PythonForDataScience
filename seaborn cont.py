import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


irisDF = sns.load_dataset('iris')
myGrid = sns.PairGrid(irisDF)
myGrid.map(plt.scatter)

plt.show()
