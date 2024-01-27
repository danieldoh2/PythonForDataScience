# # import numpy as np
# # # arr = np.arange(0,10,1)
# # # print(arr)
# # print(arr[8])
# # print(arr[0:5]) #like slicing lists, first param is inclusive, 2nd is exclusive
# # print(arr[:5])
# # print(arr[5:])
# # arr[0:5] = 100 #broadcasting. sets all elements from indices 0-4 equal to 100
# # print(arr)

# #IMPORTANT INFORMATION!!!
# #IF YOU WANT TO COPY AN ARRAY, YOU MUST SET A NEW VARIABLE EQUAL TO A COPY METHOD OF ITSELF
# copy_of_array = arr.copy()
# copy_of_array[:] = 24
# #IF YOU DO NOT DO THIS, CHANGES ON THE COPIED ARRAY WILL AFFECT THE ORIGINAL ARRAY. PYTHON DID THIS TO SAVE MEMORY ON ARRAYS

# # j = arr[0:5]
# # # j[:] = 24
# # print(arr)
# # print(copy_of_array)
# array_2d = np.array([[5,10,15], [20,25,30],[35,40,45]])
# # SLICING!!!!!
# print(array_2d[2][1])
# # print(array_2d[2,1])
# # print(array_2d[:2,1:])
# # print(array_2d[1:,:])
# #CONDITIONAL SELECTION!!!!!!!!!!!!!
# # d = np.arange(1,11)
# # boolarray = d > 5 # creates an array of the previous array with all elements replaced by TRUE AND FALSE, based on the condition
# # print(boolarray) #see the array
# # print(d[boolarray]) #use the boolean array to get a subarray of the previous array. The elements will only contain true elements
# # print(d[d>5]) #simplify the previous process into 1 step, without creating boolean array
# # arr2d = np.arange(0,50).reshape(5,10)
# # print(arr2d)
# # print(arr2d[1:2, 3:5])
# # print(arr2d[arr2d > 12 & arr2d < 15])
# # print(np.random.randn(25))
