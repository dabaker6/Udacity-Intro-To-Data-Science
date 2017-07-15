# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:45:22 2017

@author: bakerda
"""

import math

#https://en.wikipedia.org/wiki/Welch's_t-test
def welcht_test(N1,N2,u1,u2,Var1,Var2):
    t = (u1-u2)/(math.sqrt((Var1/N1)+(Var2/N2)))
    v = ((Var1/N1)+(Var2/N2))**2/((math.sqrt(Var1)**4)/((N1**2)*(N1-1))+(math.sqrt(Var2)**4)/((N2**2)*(N2-1)))
        
    return t,v

print(welcht_test(150,165,0.299,0.307,0.05,0.08))