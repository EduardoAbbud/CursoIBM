# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:17:22 2023

@author: CDW2

Escreva um programa que recebe como entradas (utilize a função input) dois 
números inteiros correspondentes à largura e à altura de um retângulo, 
respectivamente. O programa deve imprimir, usando repetições encaixadas 
(laços aninhados), uma cadeia de caracteres que represente o retângulo 
informado com caracteres '#' na saída.
"""
l=int(input("digite a largura: "))
h=int(input("digite a altura: "))
i=1
j=1
while i<=h:
    while j<=l:
        print("#",end='')
        j += 1
    i += 1
    j = 1
    print("")