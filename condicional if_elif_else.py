# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:16:07 2021

@author: user
""" 
acl=int(input("Ingrese el # de ACL"))
if acl>=1 and acl<=99:
     print("Es un acl estandar")
 
elif acl>=100 and acl<=199:
     print("Es un acl extendida")
else:
      print("No es un # de ACL válido")
     
        