# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:32:52 2019

@author: Satya Manepalli
"""

import numpy as np
import pandas as pd
arr = np.arange(10)
print(arr)
print(arr[5:8])
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
#print("Array slice = ",arr_slice)
arr_slice[1] = 12345
#print("Array, showing effect of changed slice: ", arr)

arr_slice[:] = 64
#print(arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(arr2d[1])

#print(arr2d[1][2])
#print(arr2d[1,2])

sl1 = arr2d[:2]
#print(sl1)

#array = np.array([[1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4,4],
#                  [5,5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6,6],[7,7,7,7,7,7,7,7,7,7],[8,8,8,8,8,8,8,8,8,8]])
#print (array)

#arr1=array[:1]
#print (arr1)
#arr1=array[7:]
#print (arr1)

a = np.arange(80).reshape(8, 10)
print (a)

array_2d = np.random.randint(0,100,(5,6))

a = np.random.randn(10)
print (array_2d)

b = np.random.randn(30).reshape(3,10)
#print (arr)

c = np.random.randn(40).reshape(5,2,4)
print (c)

a[4:7] = -5
#print (a)

b[2] = -8
#print (b)

c[2,1,3]=-10
#print (c)

"""points = np.arange(-5,5,0.01)  # 1000 equally spaced values
xs, ys = np.meshgrid(points, points)
print(ys)
print(ys)
#Evaluate sqrt(x^2 + y^2) across a regular grid of values
z = np.sqrt(xs**2 + ys**2)     #One statement, no loop
print(z)"""


"""points = np.arange(1,5,1)  # 1000 equally spaced values
xs, ys = np.meshgrid(points, points)
print(ys)
print(ys)
#Evaluate sqrt(x^2 + y^2) across a regular grid of values
z = np.sqrt(xs**2 + ys**2)     #One statement, no loop
print(z)

import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond,xarr,yarr)
print(xarr)
print(yarr)
print(result)"""

array = np.random.randint(-10.0,+10.0,(6,3))
#print (array)
rounded = np.around(array, decimals = 2)
#print (array)
#coverting array into dataframe Df
arrayDf = pd.DataFrame(array)
#print (arrayDf)
#6x1 array creation
IDs = np.random.randint(1000,9999,(6,1))
IDDf = pd.DataFrame(IDs, columns = ["IDs"])
print (IDDf)

IDDf['IDs']="XXXX"
#print (IDDf)

array = np.random.randint(1,10,(5,5))
#print (array)
#mean
#print (array.mean())
#sum
#print (array.sum())
#print("{:8.2f}".format(rounded.mean()))
import random
import matplotlib.pyplot as plt
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])

nsteps = 1000
draws = np.random.randint(0,2, size = nsteps)
steps = np.where(draws>0, 1, -1)
print(">>>>>>>>>>>>>>>>>>>\n",steps[:100])
walk2 = steps.cumsum()
plt.plot(walk2[:100])

 








