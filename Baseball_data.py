# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:52:53 2017

@author: bakerda
"""

import pandas as pd

baseball_data = pd.read_csv('Master.csv')

baseball_data['BMI'] = (baseball_data['weight']/2.2)/(((baseball_data['height']*2.54)/100)**2)

print(baseball_data)

baseball_data.to_csv('baseball_data_with_BMI.csv')

baseball_data['nameFull'] = baseball_data['nameFirst']+" "+baseball_data['nameLast']

print(baseball_data)