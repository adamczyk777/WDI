import random
import time

lista = [None] * 100


def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for x in range(n):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
    return arr


def selection_sort(arr):
    for start in range(len(arr)):
        for index in range(start, len(arr)):
            if arr[start] >= arr[index]:
                arr[start], arr[index] = arr[index], arr[start]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        el = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > el:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = el
    return arr


def heap_sort(lst):
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

    def siftdown(lst, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(lst) - 2) // 2, -1, -1):
        siftdown(lst, start, len(lst) - 1)

    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst


def quick_sort(arr):

    less = []
    equal = []
    bigger = []

    if len(arr) > 1:
        pivot = arr[len(arr) // 2]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                bigger.append(x)

        return quick_sort(less) + equal + quick_sort(bigger)
    else:
        return arr


for n in range(100):
    lista[n] = random.randrange(1, 101, 1)

print(selection_sort(lista))

for n in range(100):
    lista[n] = random.randrange(1, 101, 1)

print(bubble_sort(lista))

for n in range(100):
    lista[n] = random.randrange(1, 101, 1)

print(insertion_sort(lista))

for n in range(100):
    lista[n] = random.randrange(1, 101, 1)

print(heap_sort(lista))

listaB = [None] * 10
for n in range(10):
    lista[n] = random.randrange(1, 101, 1)

print(quick_sort(lista))
