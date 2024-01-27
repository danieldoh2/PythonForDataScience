import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#
tips = sns.load_dataset('tips')
# print(tips.head())
#DISTRIBUTION PLOTS

#distplot. shows distribution of univariant (1 variable) set of observations
# print(tips)
# displt = (sns.displot(tips['total_bill'], kde = False, bins = 10))

#joint plot. shows distribution of bivariant data (2 variables).
# jntplot = sns.jointplot(x = 'total_bill' , y = 'tip', data = tips)
#X and Y are two different columns that you want to compare. #Kind param lets you
#choose which way you want to visualize the data. It is automatically set to a
#scatter plot, but you can switch it to hexagon or others.

# pairplot = sns.pairplot(tips, hue = 'day', palette = 'coolwarm') #A pair plot will make return
# jointplots for every single combination of columns to compare. Keep in mind, as your dataframe gets
#larger, this will take more time to do, because there are a lot more combinations.
#To create a pairplot, all you need to do is pass in the dataframe into the parameter
#and it'll automatically read all the numerical columns for comparison. You can
# also specify a hue parameter, which is a categorical column, meaning it has
#categories, often strings. These are often male/female, yes/no, etc. Once it has this
#hue parameter, it will color and distinguish the values of the graphs.

# rugplot = sns.rugplot(tips['total_bill'])


#CATEGORICAL PLOTS
# barplot = sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std)
#Estimator param is an aggregate function applied to x and y. The pre-set estimator
#function is the average.
# countplot = sns.countplot(x = 'sex', data = tips)
#The countplot just counts the occurences of your x categorical value.

# boxplt = sns.boxplot(x = 'day', y = 'total_bill', data = tips)
#Shows distribution of data, so we can extract assumptions between the comparisons
#of two variables
# violinplt = sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex')
#Violin plot is very similar to box plot

# strplt = sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True, hue = 'sex', split = True)
#Strip plot is basically a categorical distribution plot

# swrmplot = sns.swarmplot(x = 'day', y = 'total_bill', data = tips)
#
# factorplot = sns.factorplot(x = 'day', y = 'total_bill', data = tips, kind = 'bar')
#This is a way to generally call any type of plot. You just need to specify the
#kind parameter. You could do this or call the specific plot method


#Matrix plots
# flights = sns.load_dataset('flights')
#In order for your heat maps to work properly, you must have your data in matrix
#form, meaning the rows name and the column names must match up.
# print(tips.corr())
#The .corr method will set your data set into matrix form with correlating data
# tc = tips.corr()
# print(sns.heatmap(data =tc, annot = True, cmap = 'coolwarm'))

# myg = flights.pivot_table(index = 'month', columns= 'year', values = 'passengers')
# plt.show()
#You can also set your data into matrix form using pivot tables, of course.
#You need to specify the index (rows), columns and values.
# print(myg)
# print(sns.heatmap(myg, linecolor = 'white' , linewidths = 1))
#linecolor can separate the squares in the heatmap and linewidth will change
#how thick those separating lines are.

#ClusterMap
# print(sns.clustermap(myg, cmap = 'coolwarm', standard_scale = 1 ))
#A clustermap will try to group columns and rows together by their similarities in
#the data. This will likely deorganize the columns and rows, but we're looking for
#similarities here, so that won't be an issue.


#PAIRGRIDS
iris = sns.load_dataset('iris')
# irisGrid = sns.PairGrid(iris)
# irisGrid.map(plt.scatter) #map method can allow you to apply a func to all of
#the subplots within your figure. So if we wanted to transform them all into scatterplots,
#we could.
# irisGrid.map_upper(sns.kdeplot)
# irisGrid.map_lower(sns.stripplot)
# irisGrid.map_diag(sns.violinplot)
#IMPORTANT!!! TO SPECIFY WHICH GRAPHS YOU WANT TO APPLY THE MAP FUNC TO, WRITE
#MAP AND UNDERSCORE: .MAP_ This will allow you to choose a variety of different methods


#FACET GRIDS.
# graph = sns.FacetGrid(data = tips, col = 'time', row ='smoker')
# graph.map(sns.histplot, 'total_bill') #The thing that's neat about facet grids is
#that we can apply functions to specific rows and columns through its params.
#Basically, for facet grids, we use columns and rows to frame the data on the graphs
#Then when we actually apply the map method, we need to clarify which column we
#actually want the data to be composed of. (The content)
# graph.map(sns.kdeplot, 'total_bill', 'tip')
#BUT IF WE'RE MAPPING A GRAPH THAT REQUIRES BIVARIANT DATA: WE MUST CLARIFY A
#SECOND COLUMN
# graph.map(sns.scatterplot, 'total_bill', 'tip')

#Regression Plots
# lmplot = sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex' , markers = ['o', 'v'],
#                     scatter_kws = {'s': 100})
#Like matplotlib, we can also change markers --, 'o', and change the scatter_kws for size
# newplot = sns.lmplot(x = 'total_bill', y = 'tip', data = tips, col = 'sex', row = 'time')
#Something we can also do is instead of using color (hue) to distinguish values on the
#the graph, we can pass in a row or col parameter to get two separate graphs with
# different vals. We can still use hue if we need to
anotherplot = sns.lmplot(x = 'total_bill', y = 'tip', data = tips,
                         col = 'day', aspect = 0.8, height = 8)
#we can also modify the aspect and size. aspect is the ratio of the height
#and width. Size
dict()

sns.countplot()
#Style and Color!!!!!!
sns.set_style('darkgrid') #setting the background of a figure
sns.despine(left = True, bottom= True) #You can get rid of spines of a graph.


plt.show(block = True)

