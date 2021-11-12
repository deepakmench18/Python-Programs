# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:08:23 2021

@author: Deepak Mench
@Title : Gambler Program
"""
import random;
goal=200
cash=100
bet=30
while cash <= goal and cash >= bet :
   gamble=random.uniform(0,1);
   if gamble == 1 :
      cash=((cash+(bet*2)))
   else:
      cash=((cash-(bet*2)))
if cash > goal :
   print("player won")
else:
  print("Player loose");