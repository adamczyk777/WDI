# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:59:47 2016

@author: adamc
"""

for x in range(1,11):
    print() # przejście do nowego wiersza 
    for y in range(1,11):
        print("%3i" % (x*y), end='')
