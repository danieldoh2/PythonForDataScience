import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy.random import randn


np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
#In essence, DataFrames are nested series, each column (w,x,y,z) with
# respect to (a,b,c,d,e) is its own series. Each series shares its index
print(type(df['W'])) #Here, it is confirmed that a column of a dataframe
#is its own series.
print(df)
print(df['W']) #grabbing a column
print(df[['W', 'X']]) #pass in a list of columns to get grab multiple of them
#must be double bracketed since it is a list inside bracket notation
df['newcolumn'] = df['W'] + df['Y']#You can directly declare new columns
#to add them in
df['ex'] = [3,2,3,4,1] #Ex 2 of directly adding new column
#However, the amount of vals declared like this must match the pre-existing
print(df)
df.drop(labels='ex', axis =1, inplace=True) #Dropping a column.
#Inplace must be true for the changes to be permanent
print(df)
df.drop('E', axis =0, inplace=True) #To drop a row, you don't need clarify
#the axis since the default param of axis is equal to 0 (the row param)
print(df)
print(df.shape)
print(df.loc['A']) #Grabbing rows. MUST USE BRACKET NOTATION!!!!
print(type(df.loc['A'])) #Rows are also series with respect to columns
print(df.iloc[2]) #Can also grab rows by using numerical index of row
print(df.loc['C', 'Z']) #grabbing an individual value inside of a dataframe
print(df.loc[['A', 'B'],['W', 'X']]) #grabbing multiple vals

#Conditional Selection!!!
booldf = df >0
print(df.loc['A', 'W'] > 0)
#The reason why we do conditional selection with columns is to avoid null values
print(df['W'] > 0) #Filter Statement
print(df)
print(df[df['W'] > 0]) #By doing this, we are asking the dataframe to provide
#us with a dataframe only with rows where a column W is > 0, or where it is True
print(df[(df['W'] > 0) & (df['Y'] >1)]) #If we want to do multiple conditions,
# #we must use the & operator while separating them with parenthesis
df.reset_index(inplace = True) #To reset the index, we use the .reset()
#method. To make sure it saves, we must set inplace = True. This method
# #sets the old index into its own new column
print(df)
newIND = 'CA NY WY OR CO'.split() #nifty way to create a list without commas
df['States'] = newIND #declaring new column equal to the 5 elements of new list
# print(df)
df.set_index('States', inplace= True) #This will declare a column as the new index. However,
# #the old index will not remain as a new column, unlike reset_index.
# #You still must set inplace = True to save the command
# print(df)
#Index Levels with DataFrames!!!!!
outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside)) #zip function combines the two
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
newdf = pd.DataFrame(randn(6,2), hier_index, ['A', 'B']) #notice how we're
#setting hier_index to the index of the dataframe. That means that both
#elements in each pair of tuples is an index. They merely stack upon eachothr.
print(newdf)
print(newdf.loc['G1'].loc[1]) #To grab nested indices, you must attach a
#new call to the method .loc
print(newdf.loc['G2'].loc[2]['B']) #if we wanted to grab a specific value,
#you just attach the column name. Basically, you work outsides --> inside
#left --> right
newdf.index.names = ['Gay', 'Guard'] #Naming the indices (different types
#of rows).
print(newdf.loc['G1'])
print(newdf.xs(1, level = 'Guard')) #This function makes it easier to grab
#specific values.
df['G1'].map()
