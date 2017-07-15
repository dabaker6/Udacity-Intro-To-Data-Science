# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:13:49 2017

@author: bakerda
"""

import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    m = len(values)
    cost_history = []

    for i in range (num_iterations):
        
        h = numpy.dot(features, theta)
        
        theta = theta - alpha / m * numpy.dot((h-values),features)
        
        cost = compute_cost(features, values, theta)
        
        cost_history.append(cost)

    return theta, pandas.Series(cost_history) # leave this line for the grader
