# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:35:48 2023

@author: CDW2
"""

def testePrimo(num):
    #num = int(input("Número: "))
    i = 2
    primo = True
    while i < num and primo:
        resto = num % i
        i += 1
        if resto == 0:
            primo = False
    return primo

print("Programa irá parar quando digitado um número negativo!!!")
n=1
while n>=0:
    n=int(input("Entre com o número a ser testado: "))
    primo=testePrimo(n)
    if primo:
        print("primo")
    else:
        print("não primo")
