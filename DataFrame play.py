# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:48:11 2017

@author: bakerda
"""

import pandas as pd
import numpy as np

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea', 
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
    #create dictionary, keys = column names, data = pandas series with data from above lists
olympic_medal_counts = {'country_name' : pd.Series(countries),'gold' : pd.Series(gold), \
'silver' : pd.Series(silver),'bronze' : pd.Series(bronze)}    
    
df = pd.DataFrame(olympic_medal_counts)


print(df)

print(df['country_name'])

print(df[['country_name','gold']])

print(df.loc[18])
print("")
print("Return all columns when gold >=10:")
print(df[df['gold']>= 10])
print("")
print("Just return country name:")
#print country_name from dataframe where the gold column in >=10
print(df['country_name'][df['gold'] >=10])

#can treat as objects!
print(df.gold)

print([(df.silver >1) & (df.gold >1)])


print(np.mean(df['bronze'][df['gold']>=1]))

avg_medal_count = df[['gold','silver','bronze']].apply(np.mean)

print (avg_medal_count)

