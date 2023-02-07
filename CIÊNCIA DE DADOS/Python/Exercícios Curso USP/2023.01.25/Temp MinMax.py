# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:05:35 2023

@author: CDW2
"""

def MinMax(temperaturas):
    print(mínima(temperaturas))
    print(máxima(temperaturas))
    
def mínima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def máxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

LTemps = [1, 2, 3, 4, 5, 6, 7, 0, 9, 99, 45, 65, -53, -8, 66]
MinMax(LTemps)