# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:33:59 2023

@author: CDW2

Exercício 1 - Primos

Escreva a função n_primos que recebe como argumento um número inteiro maior 
ou igual a 2 como parâmetro e devolve a quantidade de números primos que 
existem entre 2 e n (incluindo 2 e, se for o caso, n).
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

def n_primos(n):
    i=2
    cont=0
    while i<=n:
        if testePrimo(i)==True:
            cont+=1
        i+=1
    return cont

n=int(input("Entre com o número a ser analisado: "))
print(n_primos(n))
