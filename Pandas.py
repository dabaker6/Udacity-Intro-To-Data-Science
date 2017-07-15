# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:56:19 2017

@author: bakerda
"""
import numpy as np
import pandas as pd

d = {'one':pd.Series([1,2,3], index=['a','b','d']),'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)

print (df)
print("")
print("just series One:")
print (df['one'])
print("")
print("If greater than 3")
print(df > 3)
print(df[df>2])

print(df.apply(np.mean))

print(df['one'].map(lambda x: x>=1))

print(df.applymap(lambda x: x>1))

print(df.dtypes)
print(df.describe)