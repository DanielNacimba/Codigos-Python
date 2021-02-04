# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:33:06 2021

@author: user
"""

while True:
    x= input("Ingrese el numero para contar: ")
    if x=='q' or x=='salir':
        break
    
    x=int (x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break