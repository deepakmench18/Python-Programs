# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:29:49 2021

@author: Deepak Mench
@Title : Quartic Equation
"""
import math

try:
    a= float(input("Enter value of a : "))
    b=float(input("Enter value of b : "))
    c = float(input("Enter value of c : "))

    delta = b * b - 4 * a *c 
    sqrtOfdelta= math.sqrt(abs(delta))                  

    if delta > 0:  
        print((-b + sqrtOfdelta) / (2 * a))  
        print((-b - sqrtOfdelta) / (2 * a)) 
except:
    print("Please enter valid Values");


