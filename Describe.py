# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:30:03 2017

@author: bakerda
"""

import pandas as pd

baseball_data = pd.read_csv('Master.csv')

print(baseball_data.describe(include = 'all'))