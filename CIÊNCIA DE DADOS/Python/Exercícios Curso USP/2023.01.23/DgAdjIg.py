num=input("Entre com o número a ser analisado: ")
tamanho=len(num)
num=int(num)

seqIg = False
i=0

while not seqIg and i<tamanho:
    ult = num//(10**i)%10
    penul = num//(10**(i+1))%10
    if ult==penul:
        seqIg = True
    else:
        i+=1
if seqIg and tamanho!=1:
    print("sim")
else:
    print("não")
