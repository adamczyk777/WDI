import random
import os
import time

height = int(input("enter height: "))
width = int(input("enter width: "))
indexes = [None] * height
for z in range(500):
    rnd = random.randint(0, width)
    for y in range(len(indexes)-1, 0, -1):
        indexes[y] = indexes[y-1]
    indexes[0] = rnd
    for x in indexes:
        for n in range(width):
            if n == x and n == width-1:
                print("x")
            elif n == x:
                print("x", end='')
            elif n == width-1:
                print(" ")
            else:
                print(" ", end="")
    time.sleep(0.3)
    os.system('cls')