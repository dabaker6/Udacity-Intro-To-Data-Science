# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:03:08 2017

@author: bakerda
"""

import pandas
import pandasql
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
aadhaar_data = pandas.read_csv('aadhaar_data.csv')
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

q = """SELECT registrar,enrolment_agency FROM aadhaar_data LIMIT 50;"""

print(pandasql.sqldf(q.lower(), locals()))    
