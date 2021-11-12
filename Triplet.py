# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:00:05 2021

@author: Deepak Mench
@Title: Sum of Three Interger add to zero
"""

def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
    if (found == False):
        print(" not exist ");
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)