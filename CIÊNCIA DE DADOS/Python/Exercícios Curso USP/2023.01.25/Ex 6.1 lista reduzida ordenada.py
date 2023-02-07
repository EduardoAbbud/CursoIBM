# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:03:03 2023

@author: CDW2

Escreva a função remove_repetidos que recebe como parâmetro uma lista com 
números inteiros, verifica se tal lista possui elementos repetidos e os remove.
A função deve devolver uma lista correspondente à primeira lista, sem elementos
repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
"""

def remove_repetidos(lista):
    #apaga = False
    i=0
    while i < len(lista):
        j=i+1
        while j < len(lista):
            if lista[i] == lista[j]:
                del lista[j]
                j-=1
            j+=1
        i+=1
    return sorted(lista)

"""
lista = [7,3,33,12,3,3,3,7,12,100]
lista_red = remove_repetidos(lista)
lista_ord = sorted(lista_red)
print(lista_red)
print(lista_ord)
"""