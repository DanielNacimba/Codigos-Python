# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:38:33 2021

@author: user
"""

lista=['R1',5,5.8,True,"R1"]
print(lista)
print(type(lista))
print(len(lista))
print(lista[0],'\n')
print(lista[4],'\n')
print(lista[-1],'\n')
print(lista[-5],'\n')
print(lista[-2],'\n')
lista[3]=False
print(lista)
del lista[4]
print(lista)
print(len(lista))
print(lista)
lista.append("R2")
print(lista)
lista.append("R3")
print(lista)

