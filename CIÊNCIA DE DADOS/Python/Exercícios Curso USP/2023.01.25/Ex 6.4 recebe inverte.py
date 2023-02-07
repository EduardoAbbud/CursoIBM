# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:55:02 2023

@author: CDW2

Exercício 2 - Invertendo sequência

Como pedido na primeira video-aula desta semana, escreva um programa que recebe
uma sequência de números inteiros e imprima todos os valores em ordem inversa. 
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer 
parte da sequência.
"""

lista_user = []
n=1
while n!=0:
    n=int(input("Digite um número: "))
    if n!=0: lista_user.append(n)

lista_inv = []
for j in range(len(lista_user),0,-1):
    lista_inv.append(lista_user[j-1])
#print(lista_user)
for i in lista_inv:
    print(i)