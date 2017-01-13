# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:20:32 2016

@author: adamc
"""
import time
start_time = time.time()
import math
upperBound = 10000
isPrime = [True] * (upperBound +1)
isPrime[0] = False
isPrime[1] = False
for x in range(2, int(math.sqrt(upperBound)+1) ):
    if isPrime[x] != False:
        for k in range(x**2, upperBound + 1 , x):
            isPrime[k] = False
for z in range (2, upperBound+1):
    if isPrime[z] == True:
        print(str(z) + " ", end="")
        
print("--- %s seconds ---" % (time.time() - start_time))
