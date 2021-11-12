# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:33:09 2021

@author: Deepak Mench
@Title : Prime Factor
"""

def primeFactor(N) :
		for i in range(2,N):
			while(N%i==0):
				print(i , " ");
				N = N/i;
		if(N>2):
			print(N);
N = int(input("Enter Number :"));
primeFactor(N);