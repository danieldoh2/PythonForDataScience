import numpy as np
import pandas
import pandas as pd
import html5lib
import sqlalchemy
import lxml
import xlrd
import openpyxl
from sqlalchemy import create_engine


#Filling

# dic = {'A':[1,2,np.nan] , 'B':[5,np.nan,np.nan] , 'C':[1,2,3]}
# df = pd.DataFrame(dic)
# print(df)
# # df.dropna(axis = 1, inplace=True) #This function, with param 1, will
# # #automatically drop any columns with any null values
# # df.dropna(inplace= True) #This will drop any rows with null values. Again,
# # we don't need to clarify the axis param since rows are index 0
# # df.dropna(thresh=2, inplace= True) #Here, the threshold gives a min amount of
# # non-Null values required to not get dropped. In this case, it needs 2
# # df.fillna(value= 'FILL VALUE', inplace= True) #This method will fill in any
# #null values with the value parameter in the method definition
# print(df)
# df['A'].fillna(value = df['A'].mean(), inplace = True) #Here, we are directly
# #filling in the null values of column A with its average. #You can do this
# #process with other methods besides mean (average).
# print(df)

#Groupby
# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
#        'Sales':[200,120,340,124,243,350]}
# #Remember, when passing a dictionary into a dataframe, the keys become the
# #columns and the range of numbers is assigned as a row index (1,2,3,n). The
# #values just work downwards from the column. ALL KEYS must have vals/lists
# #of equal length
# newdf = pd.DataFrame(data)
# #Be careful. When passing in a dictionary, the values can not be scalar
# #(singular), as in single string, int, etc. It must be a list, or the index
# #param must be set to [0] if you want to use scalar values.
# print(newdf)
# bycomp = newdf.groupby('Company') #Whatever column we use will have its data
# #become the new index(rows)
# #We group the dataframe together and then we perform an aggregate function
# #on all of it
# print(bycomp.sum())
# print(bycomp.std().loc['GOOG'])
# #Aggregate functions and we can attach other methods to get row values
# print(newdf.groupby('Company').describe())

# #Merging,Joining,Concatenating
# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
#                         'B': ['B0', 'B1', 'B2', 'B3'],
#                         'C': ['C0', 'C1', 'C2', 'C3'],
#                         'D': ['D0', 'D1', 'D2', 'D3']},
#                         index=[0, 1, 2, 3])
# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
#                         'B': ['B4', 'B5', 'B6', 'B7'],
#                         'C': ['C4', 'C5', 'C6', 'C7'],
#                         'D': ['D4', 'D5', 'D6', 'D7']},
#                          index=[4, 5, 6, 7])
# df3 = pd.concat([df1,df2])
# print(df3)
# #To get the data to truly concatenate and add up, you must make sure the
# #keys are the same since they will become columns. If the columns aren't the
# #same, the concat method won't know how to store the data, and you'll get a
# #bunch of null vals
# df4 = pd.concat([df1,df2], axis = 1)
# #Concatenating on the columns. The keys will still be the columns, but they will
# #add up on the columns instead, creating multiple columns with same name
# print(df3)
# print(df4)

# #Merging
# left = pd.DataFrame({'A': ['K0', 'K1', 'K2', 'K3'],
#                      'key': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'C': ['K0', 'K1', 'K2', 'K3'],
#                       'key': ['Abillion', 'A1', 'A2', 'A3',],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
#
# merge2 = pd.merge(left, right, on= 'key')
# print(merge2)
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
# print(pd.merge(left,right, how = 'outer', on = ['key2', 'key1']))
#When using how = 'inner', merging dataframes with two keys will look for
#pairs of key values that are in the intersection, meaning both keys from
#both dataframes will have the same pairs. So, in this case, key1 and key2 from
# the left and right dataframes both have (K0, K0) once and (K1,K0), the right
#dataframe having it twice and the left having it once. Now that it has all of its similar pairs,
#it'll print out all the elements at the same indices as the key pairs from both dataframes
#The how = 'outer' will take the UNION, meaning it will take all key pairings
#and provide the values at the index (row) of each of the key pairings. If
#there isn't a value for a certain key pairing, which likely will happen,
#it'll produce a null value for it.

#JOINING!!!
#the same process as
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                      'B': ['B0', 'B1', 'B2']},
#                       index=['K0', 'K1', 'K2'])
#
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                     'D': ['D0', 'D2', 'D3']},
#                       index=['K0', 'K2', 'K3'])
# print(right.join(left))
#Joining is the same thing as merging. If you don't specify the how parameter,
#it'll automatically just take the row index of the first dataframe. If you
# specify the inner (intersection) or outer(union).

#Pandas operations
dataF = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,111],'col3':['abc','ghi','def','xyz']})
#Quick method to return a row of a dataframe. the int param is how many u want
#if you want the whole thing, don't enter a number.
# print(dataF['col1'].unique()) #method that returns all unique elements
# print(dataF.loc[0].nunique()) #method that returns the number of unique elements
# print(dataF['col2'].value_counts()) #method to spread out all the elements and
# # see how many times they occurred.
# print(dataF[(dataF['col1'] > 2) & (dataF['col2'] == 111)]) #return me a dataframe with the rows of when
# #column 1 has values greater than 2 AND where column 2 has a value equal to 111
# def times2(num):
#     return num * 2
# print(dataF['col1'].apply(times2)) #This is a method that we can use to apply
# #our own functions to columns or rows of a dataframe. Make sure you don't include
# #the parenthesis after you type the function.
# print(dataF.columns) #Can directly call a funct
# print(dataF)
# print(dataF.sort_values('col3')) #A way to sort the values of a column inside
# a dataframe. Be careful, this will change the order of the index, which will
#alter the order of the other values in other columns.
# print(dataF.isnull()) #A quick method that checks a dataframe for null values,
#It will return a dataframe containing boolean values that reflect whether or
#not an element in the original dataframe was null.
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','x','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
# print(df)
print(df.pivot_table(values= 'D', index= ['A','B'], columns= ['C']))
# Here we are creating a pivot table with a multi-layered index.


#Data entry.
# d = pd.read_csv(r'C:\Users\dohd\Downloads\Py_DS_ML_Bootcamp-master\Refactored_Py_DS_ML_Bootcamp-master\03-Python-for-Data-Analysis-Pandas\example')
# print(d)
# d.to_csv('My_output', index = False) #Saving our dataframe into a new csv file
# called My_output. Setting the index = false will save the dataframe's old index
# print(pd.read_csv('My_output'))
# print(pd.read_excel(r'C:\Users\dohd\Downloads\Py_DS_ML_Bootcamp-master\Refactored_Py_DS_ML_Bootcamp-master\03-Python-for-Data-Analysis-Pandas\Excel_Sample.xlsx'))
# data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
# print((data))
# print(data[0])
# engine = create_engine('sqlite:///memory:')
# d.to_sql('my_table', engine)
# sqldf = pd.read_sql('my_table', con = engine)
d = {'num_legs': [4, 4, 2, 2],
     'num_wings': [0, 0, 2, 2],
     'class': ['mammal', 'mammal', 'mammal', 'bird'],
     'animal': ['cat', 'dog', 'bat', 'penguin'],
     'locomotion': ['walks', 'walks', 'flies', 'walks']}
dfs = pd.DataFrame(data=d)
dfs = dfs.set_index(['class', 'animal', 'locomotion'])
print(dfs)