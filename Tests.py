# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:10:48 2017

@author: bakerda
"""
#########################################################################

import numpy as np
import scipy.stats
import random
import matplotlib.pyplot as plt
import math
#T-Test

#Shapiro-Wilk

def Normal_Shapiro(data):
    w,p = scipy.stats.shapiro(data)
    
    if p<0.05:
        h0 = "Reject null hypothesis: data is not normally distributed"
    elif p>=0.05:
        h0 = "Accept null hypothesis: data is normally distributed"
    
    return w,p,h0

#w = test statistic
#p = p value - given the h0 that data is drawn from a normal distribution what is the
#               likelihood that W was at least as extreme than the observed W.

#Mann Whitney U


#x = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (i - mu)**2 / (2 * sigma**2) )


def normal_dist(mu,sigma,sample_size):
    data = np.random.normal(mu, sigma, sample_size)
    return data    

def random_dist(sample_size):
    data = []
    
    for i in range (0,sample_size):
        data.append([])
        x = random.randint(0,sample_size)
        data[i].append(x)

    return data

def log_dist(sample_size):
    data = []
    
    for i in range (0,sample_size):
        data.append([])
        x = math.log(i+1)
        data[i].append(x)

    return data    

mu, sigma,sample_size = 50, 0.1, 1000 

data = normal_dist(mu,sigma,sample_size)

plt.plot(list(range(0,sample_size)),data)
plt.show()

print(Normal_Shapiro(data))


data = random_dist(sample_size)

plt.plot(list(range(0,sample_size)),data)
plt.show()

print(Normal_Shapiro(data))

data = log_dist(sample_size)

plt.plot(list(range(0,sample_size)),data)
plt.show()

print(Normal_Shapiro(data))