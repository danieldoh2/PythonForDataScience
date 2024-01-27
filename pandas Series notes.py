import turtle

import pandas
import pandas as pd
import numpy as np
from pandas import Series
import turtle as tr

#SERIES!!!

t1= turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
labels = [t1, t2, t3]
my_data = [10,20,30]
# arr = np.array(my_data)
dict = {'i1':30, 'i2':45, 'i3':60}
dict2 = {'Beta':"DanielA", 'Alpha':"DannyD", 'Sigma':"DanielD"}
dict3 = {'i1':31, 'i2':46, 'i3':61}
#Dictionaries can be directly inputted into series, with key being index,
#value being data
print(Series(data = my_data, index= labels))
print(Series(data = my_data, index= labels))
s1 = Series(dict)
s2 = Series(dict2)
# s3 = Series(my_data, labels) #first param is data, second is index
s4 = Series(dict3)
# # print(s1[2]) #grabbing a value uses the index (can be string, int, etc)
print(s2['Sigma']) #grabbing a value uses the index (can be string, int, etc)
print(s3[t1])
print(s3)
addition = s1 + s4 #if you do operations on series objects, it'll line up the
# #indices and perform operations on the data with the same indices
print(addition)
print(s1)