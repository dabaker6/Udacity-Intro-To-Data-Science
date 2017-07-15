# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:43:41 2017

@author: bakerda
"""

from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/
    
    
    gg = ggplot(pandas.read_csv(hr_year_csv),aes('yearID','HR'))+ \
    geom_point(colour='red')+ \
    geom_line(colour='red') + \
    ggtitle('Total Home Runs By Year')+ \
    xlab('Year')+ylab('HR')
        
             
    print(gg)


lineplot('hr_year.csv')

def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot.
    #
    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions. For example, 
    # ggplot(data, aes(xvar, yvar, color=category_var)). This might help you 
    # in this exercise.
    
    gg = ggplot(pandas.read_csv(hr_by_team_year_sf_la_csv),aes('yearID','HR',color='teamID'))+ \
    geom_point()+ \
    geom_line() + \
    ggtitle('Total Home Runs By Year')+ \
    xlab('Year')+ylab('HR')
        
    print(gg)

lineplot_compare('hr_by_team_year_sf_la.csv')
