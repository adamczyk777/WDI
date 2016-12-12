# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:48:40 2016

@author: adamjaku
"""

a = float(input("enter first number: "))
op = input("choose sign to determine operation : ")
b = float(input("enter the second number: "))
if op == "/":
    print(a / b)
elif op == "*":
    print(a * b)
elif op == "+":
    print(a+b)
elif op=="-":
    print(a - b)
elif op == "^":
    print(a**b)
    