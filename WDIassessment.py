# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 01:03:30 2016

@author: adamc
"""

import time
import random
def quicksort(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)//2]
        left = 0
        right = len(arr)-1
        while left <= right:
            while arr[left] < pivot:
                left = left+1
            while arr[right] > pivot:
                right = right - 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left = left+1
                right = right-1
        quicksort(arr[:right])
        quicksort(arr[left:])
    return arr
def heapSort(arr):   
    def heapify(end,i):
        l=2 * i + 1  
        r=2 * (i + 1)   
        max=i   
        if l < end and arr[i] < arr[l]:   
            max = l   
        if r < end and arr[max] < arr[r]:   
            max = r   
        if max != i:   
            arr[i], arr[max] = arr[max], arr[i] 
            heapify(end, max)   
    end = len(arr)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(i, 0)
    return arr
def bubbleSort(arr):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] > arr[y]:
                arr[x], arr[y] = arr[y],arr[x]
    return arr
def chooseSort(arr):
    for i in range(50):
        minimal = i
        for j in range (i,50):
            if arr[j] < arr[minimal]:
                minimal = j
        arr[minimal], arr[i] = arr[i], arr[minimal]
    return arr
def insertionSort(arr):
    for i in range(1,len(arr)):
        x=arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = x
    return arr
bubbleArr=[]
chooseArr=[]
insertionArr = []
heapArr = []
quickArr = []
quickArr2 = []
for n in range(10):
    testList = [0] * 50
    for n in range(50):
        testList[n] = random.randrange(1,51,1)
    bubble = time.clock()
    bubbleSort(testList)
    bubble2 = time.clock()
    bubbleArr.append(bubble2 - bubble)
    choose = time.clock()
    chooseSort(testList)
    choose2 = time.clock()
    chooseArr.append(choose2 - choose)
    insertion = time.clock()
    insertionSort(testList)
    insertion2 = time.clock()
    insertionArr.append(insertion2 - insertion)
    heap = time.clock()
    heapSort(testList)
    heap2 = time.clock()
    heapArr.append(heap2 - heap)
    quick = time.clock()
    print(testList)
    print(quicksort(testList))
    quick2 = time.clock()
    quickArr.append(quick2 - quick)
    quick2 = time.clock()
    sorted(testList)
    quick2 = time.clock()
    quickArr2.append(quick2 - quick)
print("bubblesort", sum(bubbleArr)/10)
print("wybieranie", sum(chooseArr)/10)
print("wstawianie", sum(insertionArr)/10)
print("kopcowanie", sum(heapArr)/10)
print("quicksort", sum(quickArr)/10)
print("wbudowany algorytm pythona", sum(quickArr2)/10)
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('bubblesort', 'wybieranie', 'wstawianie', 'kopcowanie', 'quickosrt', 'sorted()')
y_pos = np.arange(len(objects))
performance = [(sum(bubbleArr)/10),(sum(chooseArr)/10),(sum(insertionArr)/10),(sum(heapArr)/10),(sum(quickArr)/10),(sum(quickArr2)/10)]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Czas')
plt.title('Wydajnosc algorytmow sortowania')
 
plt.show()
