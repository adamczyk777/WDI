# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:36:41 2016

@author: adamc
"""
def clean(txt):
    import re, string;
    pattern = re.compile('[\W_]+')
    pattern.sub(txt, string.printable)
    return txt
def cezar(txt, klucz):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - int(klucz):
            zaszyfrowny += chr(ord(txt[i]) + int(klucz) - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + int(klucz))
    return zaszyfrowny
def deCezar(txt, klucz):
    odszyfrowany = ""
    klucz2 = int(klucz) % 26
    for znak in txt:
        if (ord(znak) - klucz2 < 97):
            odszyfrowany += chr(ord(znak) - klucz2 + 26)
        else:
            odszyfrowany += chr(ord(znak) - klucz2)
    return odszyfrowany
u_tekst = input("Podaj ciąg do zaszyfrowania:")
u_klucz = input("Podaj kluz z jakim szyfrujemy")
print("Ciąg zaszyfrowany:", cezar(clean(u_tekst), u_klucz))
print(deCezar(cezar(clean(u_tekst), u_klucz), u_klucz))