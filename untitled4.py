# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:20:09 2016

@author: adamc
"""

firstBase = int(input("pierwsza"))
l1 = input("Wprowadz pierwsza liczbe")
toBase = int(input("druga"))
result = 0
for el in l1:
    result += int(el)
    result *= firstBase
result /= firstBase

