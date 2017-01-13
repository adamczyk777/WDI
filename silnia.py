# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:11:31 2016

@author: adamc
"""
import time
iterations = int(input("input n to calculate n!"))
def recursive(n):
    if n == 1:
        return 1
    else:
        return n*(recursive(n-1))
def iterative(n):
    result = 1
    for el in range(1,n+1):
        result*=el
    return result
time1 = time.clock()
print(iterative(iterations))
print(time.clock() - time1)
time2 = time.clock()
print(recursive(iterations))
print(time.clock() - time2)