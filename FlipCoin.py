# -*- coding: utf-8 -*-
"""

Created on Mon Nov  8 12:28:33 2021
@author: Deepak Mench

"""
import random

numberflips = int(input("Enter how many flips you want"));
countofTail=0;
countofhead=0;
while(0<numberflips) :
        flip = random.uniform(0,1)
        if (flip<0.5) :
                     print("Tails")
                     countofTail+=1
        else :
             print("Head")
             countofhead +=1
        numberflips-=1;
print(countofhead );
print(countofTail);
percentageofHeads = (countofhead *100/numberflips);
print("Percentage of Heads : ");
print(percentageofHeads);

percentageOfTails = 100 - percentageofHeads;
print("Percentage of Tails : ");
print(percentageOfTails);