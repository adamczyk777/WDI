# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:13:43 2016

@author: adamc
"""

binary = input("wpisz liczbę w systemie binarnym: ")
result = 0
for char in binary:
    result += int(char)
    result *= 2
print(str(result//2))
