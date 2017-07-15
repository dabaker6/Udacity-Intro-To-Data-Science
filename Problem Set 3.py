# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import pandasql
import csv
import datetime

def num_rainy_days(filename):
    weather_data = pandas.read_csv(filename)
    
    q = """SELECT COUNT(Precipi) FROM weather_data WHERE Precipi >0;"""
    
    print(pandasql.sqldf(q.lower(), locals())) 
    
num_rainy_days('weather_underground.csv')

def max_temp_aggregate_by_fog(filename):
    weather_data = pandas.read_csv(filename)
    
    q = """SELECT FOG, MAX(maxtempi) FROM weather_data GROUP BY FOG;""" 
    
    print(pandasql.sqldf(q.lower(), locals()))

max_temp_aggregate_by_fog('weather_underground.csv')

def avg_weekend_temperature(filename):
    weather_data = pandas.read_csv(filename)
    
    q = """SELECT AVG(meantempi) FROM weather_data WHERE strftime('%w',date)='0' or strftime('%w',date)='6';""" 
    
    print(pandasql.sqldf(q.lower(), locals()))

avg_weekend_temperature('weather_underground.csv')

def avg_min_temperature(filename):
    weather_data = pandas.read_csv(filename)
    
    q = """SELECT AVG(mintempi) FROM weather_data WHERE mintempi > 55 AND Precipi >0;"""
    
    print(pandasql.sqldf(q.lower(), locals()))
    
avg_min_temperature('weather_underground.csv')

def fix_turnstile_data(filenames):
    
    #https://docs.google.com/document/d/1S4Gk42ZPBKAUZh7IPbqyzq_vk18oCvcniVcA4byBXCE/pub
    
    f_in = open('subway.txt','r')
    f_out = open('updated_'+'subway.txt','w')
    
    reader_in = csv.reader(f_in, delimiter=',', quoting=csv.QUOTE_NONE)
    writer_out = csv.writer(f_out)
    
    for line in reader_in:
            
        i=3
                
        for x in range(0,int((len(line)-3)/5)):
                            
            line_out = [line[0],line[1],line[2]]
            
            for y in range(i,i+5):
                line_out.append(line[y])
            i=i+5
                    
            writer_out.writerow(line_out)
        
    
    print('done')
            
fix_turnstile_data('Subway.txt')
            
def create_master_turnstile_file(filenames, output_file):
        with open(output_file, 'a') as master_file:
            master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
            for filename in filenames:
                f = open(filename,'r')
                for line in f:
                    master_file.write(line)
                    
                    
def filter_by_regular(filename):
    
    turnstile_data = pandas.read_csv(filename)
    
    turnstile_data = pandas.DataFrame(turnstile_data)
    
    turnstile_data = turnstile_data[turnstile_data['DESCn']=='REGULAR']
             
    print(turnstile_data)
    
    return turnstile_data

filter_by_regular('aadhaar_data.csv')

def get_hourly_entries(df):
    #shifts column down by 1 to allow taking the difference - be careful as shifts the column by 1, so effectively taking the
    #difference between this shifted column and not taking the difference between the current row and the previous. If working will
    #return NaN for the first row and a positive integer.
    df['ENTRIESn_hourly'] = df.ENTRIESn-df.ENTRIESn.shift(1)
    #inplace = true updates the df.
    df['ENTRIESn_hourly'].fillna(1,inplace=True)
    
    return df

def get_hourly_exits(df):
    
    df['EXITSn_hourly'] = df.EXITSn-df.EXITSn.shift(1)
    
    df['EXITSn_hourly'].fillna(0,inplace=True)
    
    return df

def time_to_hour(time):

    #http://stackoverflow.com/questions/25129144/pandas-return-hour-from-datetime-column-directly
    hour = int(time[0:2])
    return hour

def reformat_subway_dates(date):
    date_formatted = datetime.datetime.strptime(date, "%m-%d-%y")
    date_formatted = date_formatted.strftime("%Y-%m-%d")
    return date_formatted

