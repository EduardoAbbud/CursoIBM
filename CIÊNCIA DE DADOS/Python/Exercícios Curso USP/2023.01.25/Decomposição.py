# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:19:22 2023

@author: CDW2
"""

n = int(input("Entre número a ser decomposto: "))

fator = 2
multi = 0

while n>1:
    while n%fator==0:
        multi += 1
        n=n/fator
    if multi>0:
        print("fator",fator,"multiplicidade =",multi)
    fator += 1
    multi=0