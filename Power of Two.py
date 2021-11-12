# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:22:11 2021

@author: Deepak Mench
@Title: Power of Two
"""

def printPowerTwo() :
    N = int(input("Enter Number : "));
    for i in range(0,N):
        powerOfTwo = 2 ** i;
        print(powerOfTwo)
printPowerTwo()  