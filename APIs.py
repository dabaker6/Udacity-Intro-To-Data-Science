# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:55:17 2017

@author: bakerda
"""

import json
import requests

#Application name	David Baker
#API key	ef76485609e26901ec8b777b04a0739b
#Shared secret	16c58f7b8b60d8335644a6a48d381e91
#Registered to	dabaker6

url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=ef76485609e26901ec8b777b04a0739b&artist=Cher&album=Believe&format=json'

data = requests.get(url).text
print(type(data))
print(data)