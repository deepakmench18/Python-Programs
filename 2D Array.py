# -*- coding: utf-8 -*-
"""
Created on Wed Nov  10 09:38:16 2021

@author: Deepak Mench
@Title : 2D Array
"""
try:
    rows = int(input("Enter Number of rows : "))
    coloum = int(input("Enter number of coloum : "))
    arr = []
    
    for i in range(rows):
        a=[]
        for j in range(coloum):
             element= int(input("Enter element : "))
             a.append(element)
        arr.append(a)
    
    for i in range(rows):
        for j in range(coloum):
            print(arr[i][j],end = " ");
        print();   
except ValueError:
        print("please enter vaild input");