# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:45:18 2021

@author: Deepak Mench
@Title : Wind Chill
"""

try:
    temp= float(input("Enter temperature :"))
    speed = float(input("Enter windspeed  :"))
    if temp < 50 and  speed >=3 and speed < 120 :
         x = pow(windSpeed ,0.16);
         windchill = 35.74 + 0.6215 *temp +( 0.4275 * temp - 35.75 ) * x;
         print( windchill , "WindChill"))    
except ValueError:
    print("Please enter Valid Input");