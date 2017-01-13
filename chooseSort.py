# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:21:22 2016

@author: Jakub Adamczyk
"""
import time
import random
def chooseSort(arr):
    for i in range(50):
        minimal = i
        for j in range (i,50):
            if arr[j] < arr[minimal]:
                minimal = j
        arr[minimal], arr[i] = arr[i], arr[minimal]
    return arr
testList = [0] * 50
for n in range(50):
    testList[n] = random.randrange(1,51,1)
before = time.clock()
chooseSort(testList)
print(time.clock() - before)