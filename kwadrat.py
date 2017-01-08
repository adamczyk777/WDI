import os
import time
width = 11
height = 11

for n in range(200):
    for a in range(height):
        for h in range(width):
            if h == width - 1:
                print('O')
            else:
                print('O', end='')
    time.sleep(0.3)
    os.system('cls')