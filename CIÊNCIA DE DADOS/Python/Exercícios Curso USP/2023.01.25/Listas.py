# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:51:04 2023

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

nlim=int(input("Limite máximo: "))
n=1
Lprimos = []
while n<=nlim:
    primo=testePrimo(n)
    if primo:
        #print(n,end=', ')
        Lprimos.append(n)
    n+=1        
print(Lprimos)
print(len(Lprimos))

for numprimos in Lprimos:
    print(numprimos**2)
    
for i in range(0,len(Lprimos),1):
    Lprimos[i] = Lprimos[i]**3
print(Lprimos)

"""
listaStr = ["a","b","c"]
listaNum = [1,2,3]

print(listaStr)
print(listaNum)

print(listaStr[1])
print(listaNum[1])
"""