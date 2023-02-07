# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:43:55 2023

@author: CDW2

Exercício 2 - (Difícil) Soma das hipotenusas

Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um 
triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. 
Em outras palavras, h é uma hipotenusa se existem números inteiros i e j 
tais que:

h^2 = i^2 + j^2

Escreva uma função soma_hipotenusas que receba como parâmetro um número 
inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n 
que são comprimento da hipotenusa de algum triângulo retângulo com catetos 
inteiros.

Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser 
somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 
1 até n testando se o número é hipotenusa de algum triângulo e somando em 
caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço 
construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o 
comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou 
não.
"""

def é_hipotenusa(h):
    catetoOp = 1
    catetoAdj=1
    hip = False
    while catetoOp<=h:
        while catetoAdj<=h:
            if h**2==catetoOp**2+catetoAdj**2:
                hip = True
                catetoAdj=h
                catetoOp=h
            catetoAdj+=1
        catetoOp+=1
        catetoAdj=1
    return hip

def soma_hipotenusas(hipM):
    #hipM = int(input("Entre com o valor a ser analisado: "))
    #print("Para n =", hipM, "as hipotenusas são:")
    
    i = 1
    somaHs = 0
    while i<=hipM:
        if é_hipotenusa(i) == True:
            somaHs += i
            #print(i,end=', ')
        i+=1
    return somaHs

#x = int(input("Entre com o valor a ser analisado: "))
#print(soma_hipotenusas(x))













