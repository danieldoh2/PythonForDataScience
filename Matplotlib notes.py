import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# #
# x = np.linspace(0,5,11)
# y = x**2
# # print(type(x))
# # plt.plot(x,y)
# # plt.xlabel('X label')
# # plt.ylabel('Y label')
# # plt.title("My GRAPH")
# #
# # plt.subplot(1,2,1)
# # plt.plot(x,y,'r')
# #
# # plt.subplot(1,2,2)
# # plt.plot(y,x,'b')


# #Object oriented method
# # fig = plt.figure() #Creates a blank canvas
# # axes = fig.add_axes([0.1,0.1,0.8,0.8]) #Adds the axes to the figure
# # axes.plot(x,y)
# # axes.set_xlabel('X Label')
# # axes.set_ylabel('Y Label')
# # axes.set_title('Title')

# # newfig = plt.figure()
# # # axes1 = newfig.add_axes([0.1, 0.1, 0.8,0.8])
# # # # axes2 = newfig.add_axes([0.2,0.5,0.4,0.3])
# # # axes1.plot(x,y)
# # # axes2.plot(y,x)
# # #parameters for axes are how far from the left, how far from down,
# # #width (how fat), and how height (how tall)
# # newfig, axes1 = plt.subplots()
# #
# # fig,axes = plt.subplots(nrows=1, ncols=2)
# # plt.tight_layout() #makes the graphs more separated
# # # for current_ax in axes:
# # #     current_ax.plot(x,y)
# # axes[0].plot(x,y) #Can index the different graphs
# # axes[1].plot(y,x)
# # print(type(fig))

# #Figure Size and DPI
# # fig = plt.figure(figsize=(3,3)) #figsize: you pass in a tuple:
# # # width and height in inches. dpi: dots (pixels) per inch
# # axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# # axes.plot(x,x**2, label = 'X Squared') #Plotting points x,y with its own
# # # label on the graph legend
# # axes.plot(x, x**3, label = 'X Cubed')
# # axes.legend(loc = 0) #creating the legend

# # figur, ax = plt.subplots(nrows = 2, ncols= 3, figsize =[3,3])
# # ax[1][1].set_title('Plot')
# # figur.savefig('mypicture.png') #Can save figures into png, jpg files

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# # ax.plot(x,y, color = 'red') #can color your lines
# ax.plot(x,y,color = '#4E1B1B', lw = 0.3,alpha = 0.5,ls = '--',marker = 'o')
# #also can color using RGB hex codes. alpha for transparency. linestyle (ls)
# #for the line style. line width (lw) for thickness of line. Marker param
# #marks your points.
# ax.set_xlim([0,10]) #You can set limits on x and y vals. pass in a list with
# #a lower and an upper limit
# ax.set_ylim([0,10])
# plt.show()
