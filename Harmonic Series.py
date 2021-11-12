# -*- coding: utf-8 -*-
"""

Created on Mon Nov  8 12:28:33 2021
@author: Deepak Mench
@Title:Harmonic Series
"""
N=int(input("Enter Number"));
HarmonicNumber = 0;
for i in range(1,N):
	HarmonicNumber += 1/i;
print("Nth Harmonic Number of ", N,".=",HarmonicNumber);
		