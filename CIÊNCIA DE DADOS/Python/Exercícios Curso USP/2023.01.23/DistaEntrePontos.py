#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
#às coordenadas x e y de um ponto em um plano cartesiano.
#Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

x1=float(input("Entre com o x1: "))
y1=float(input("Entre com o y1: "))
x2=float(input("Entre com o x2: "))
y2=float(input("Entre com o y2: "))

#Calcule a distância entre os dois pontos.

import math
dist = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

#Se a distância for maior ou igual a 10, imprima
#longe
if dist>=10:
    print("longe")
#na saída. Caso o contrário, quando a distância for menor que 10, imprima
#perto
else:
    print("perto")

