import time
import random


def heap_sort(tab):   
    def heapify(end,i):   
        l=2 * i + 1  
        r=2 * (i + 1)   
        max=i   
        if l < end and tab[i] < tab[l]:   
            max = l   
        if r < end and tab[max] < tab[r]:   
            max = r   
        if max != i:   
            tab[i], tab[max] = tab[max], tab[i] 
            heapify(end, max)   
    end = len(tab)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        tab[i], tab[0] = tab[0], tab[i]   
        heapify(i, 0)
testList = [0] * 50
for n in range(50):
    testList[n] = random.randrange(1,51,1)
before = time.clock()
heap_sort(testList)
print(time.clock()-before)