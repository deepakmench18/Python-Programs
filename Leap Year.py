# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8  09:12:59 2021

@author: Deepak Mench
@Title : Leap Year
"""

def findLeapYear() : 
         
    InputYear = int(input("Enter year  : "));
    lengthOfYear = len(str(InputYear))
    if (lengthOfYear >= 4) :
           if InputYear % 100 != 0 and InputYear % 4 == 0 or InputYear % 400 == 0 :
                  print(InputYear ," is a leap year");
           else :
                 print(InputYear ,"  is not a leap year")
             
    else :
        print("Please enter valid year : ");
        findLeapYear()

findLeapYear()       