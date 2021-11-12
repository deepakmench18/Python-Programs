# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:27:34 2021

@author: Deepak Mench
@Title : Euclidean Distance problem
"""
import math
try:
    x = float(input("Enter value of x : "))
    y = float(input("Enter value of y : "))

    distance =math.sqrt(x*x+y*y)
    print(distance , "Euclidean Distance");

except ValueError:
    print("please enter valid input");