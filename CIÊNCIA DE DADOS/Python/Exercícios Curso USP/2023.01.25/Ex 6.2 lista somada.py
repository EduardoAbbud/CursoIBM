# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:34:40 2023

@author: CDW2

Escreva a função soma_elementos que recebe como parâmetro uma lista com números
inteiros e devolve um número inteiro correspondente à soma dos elementos da 
lista recebida.
"""

def soma_elementos(lista):
    soma=0
    for i in lista:
        soma=soma+i
    return soma

"""
lista = [5,5,5,5,0,5]
somaaaaa = soma_elementos(lista)
print(somaaaaa)
"""
