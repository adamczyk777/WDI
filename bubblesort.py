# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import time
def bubbleSort(arr):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] > arr[y]:
                arr[x], arr[y] = arr[y],arr[x]
    return arr
testList = [0] * 50
for n in range(50):
    testList[n] = random.randrange(1,51,1)
before=time.clock()
bubbleSort(testList)
print(time.clock() - before)