# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:19:08 2017

@author: bakerda
"""

import numpy as np
import pandas as pd

numbers = [1,2,3,4,5]

print(np.mean(numbers))

print(np.median(numbers))

print(np.std(numbers))

numbers = np.array([1,2,3,4,5])

print(numbers)
print("")
#can slice
print(numbers[1])
print(numbers[:2])

#slice a 2-D matrix

two_D_numbers = np.array([[1,2,3],[4,5,6]],float)

print(two_D_numbers)
print(two_D_numbers[1][1])
print(two_D_numbers[1,:])
print(two_D_numbers[:,1])

array_1 = np.array([1,2,3],float)
array_2 = np.array([4,5,6],float)

print(array_1+array_2)
print(array_1-array_2)
print(array_1*array_2)

array_1 = np.array([[1,2],[3,4]],float)
array_2 = np.array([[5,6],[7,8]],float)

print(array_1+array_2)
print(array_1-array_2)
print(array_1*array_2)

array_1 = np.array([1,2,3],float)
array_2 = np.array([[1],[2],[3]],float)

print(np.mean(array_1))
print(np.mean(array_2))
print(np.dot(array_1,array_2))

array_a = np.array([1,2,3,4,5])
array_b = np.array([2,3,4,5,6])
#array_a[0] * array_b[0] + array_a[1] * array_b[1].........array_a[n] * array_b[n]
print(np.dot(array_a,array_b))