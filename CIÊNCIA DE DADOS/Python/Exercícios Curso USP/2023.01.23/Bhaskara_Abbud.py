VarA=float(input("Entre com o valor de 'a' da eq de segundo grau: "))
VarB=float(input("Entre com o valor de 'b' da eq de segundo grau: "))
VarC=float(input("Entre com o valor de 'c' da eq de segundo grau: "))

#y=-b+-sqrt(delta)/2a
#delta=b**2-4ac

#se delta=0 --> uma raiz
#se delta hegativo --> esta equação não possui raízes reais
#se delta positivo --> as raízes são y1 e y2

import math
delta=VarB**2-4*VarA*VarC

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        y1=-VarB / ( 2 * VarA)
        print("a raiz desta equação é", y1)
    else:
        y1=(-VarB - math.sqrt(delta)) / ( 2 * VarA)
        y2=(-VarB + math.sqrt(delta)) / ( 2 * VarA)
        print("as raízes da equação são", y1,"e", y2)
        
