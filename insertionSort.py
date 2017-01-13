# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:25:02 2016

@author: adamc
"""
import random
import time
def insertionSort(arr):
    for i in range(1,len(arr)):
        x=arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = x
    return arr
testList = [0] * 50
for n in range(50):
    testList[n] = random.randrange(1,51,1)
before = time.clock()
insertionSort(testList)
print(time.clock() - before)