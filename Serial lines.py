# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:33:15 2017

@author: bakerda
"""

import sys
import string

def word_count():
    
    sys.stdin = open('Dummy.txt')
        
    word_counts = {}

    for line in sys.stdin:
        
        data = line.strip().split(" ")
        
        for i in data:
            translator = i.maketrans('', '', string.punctuation)
            key = i.translate(translator).lower()
            
            if key in word_counts.keys():
                word_counts[key] += 1
            else:
                word_counts[key] = 1

    print (word_counts)

word_count()
