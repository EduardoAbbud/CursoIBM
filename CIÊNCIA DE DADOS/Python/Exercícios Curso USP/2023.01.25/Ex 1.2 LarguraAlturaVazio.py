# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:17:22 2023

@author: CDW2

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma 
que os caracteres que não estiverem na borda do retângulo sejam espaços.
"""
l=int(input("digite a largura: "))
h=int(input("digite a altura: "))
i=1
j=1
while i<=h:
    while j<=l:
        if (j!=1 and i!=1) and (j!=l and i!=h):
            print(" ",end='')
        else:
            print("#", end='')
        j += 1
    i += 1
    j = 1
    print("")
    