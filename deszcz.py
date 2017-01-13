# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:33:18 2016

@author: adamc
"""
import os
from random import randint
import time

x = int(input("wprowadz liczbe kolumn: ")) #pobieram liczbe kolumn a poniżej wierszy
y = int(input("wprowadz liczbe wierszy: "))
print("Merry Christmas!!!") #mały easter egg
time.sleep(2) #oczekiwanie na rozpoczecie petli
indexPosition = [None]*y #deklaruje tablice o rozmiarze takim jak ilosc kolumn
while True: #nieskonczona petla podtrzymujaca animacje przy zyciu dla przerwania wystarczy ctrl+c
    os.system('cls') #czysci nam konsole za kazda iteracja
    for n in range(y-1, -1, -1): # petla przepisuje wartosci o jeden index do przodu
        indexPosition[n] = indexPosition[n - 1] # male TODO zrobić za pomocą konkatenacji odpowiednich indeksow listy
    indexPosition[0] = randint(0, x+1) # ustawia pierwszy index na nowa wartosc randomowej lokalizacji gwaizdki
    for el in indexPosition: #iteruje po naszej liscie z lokalizacja
        for n in range(x): #petla ktora drukuje odpowiednie znaki w danym wierszu, ma tyle iteracji ile wierszy
            if n != x-1: # warunek dla przypadku gdy nie mamy zaczynac od nowej linii
                if n == el:
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                if n == el: #tutaj zaczynamy od nowej linijki dlatego nie ma juz endl=''
                    print('*')
                else:
                    print(' ')
    time.sleep(0.3) # ustawiam czas odswiezania programu na 3 dziesiate sekundy, konsola sie czysci i na nowo robi program co okolo 0,3s (+ czas wykonania)
