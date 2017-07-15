# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:53:45 2017

@author: bakerda
"""

import numpy as np

def compute_r_squared(data, predictions):
    r_squared = 1-(np.sum((data-predictions)**2)/np.sum((data-np.mean(data))**2))
    
    return r_squared