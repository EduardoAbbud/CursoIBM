def fatorial(num):
    #num = int(input("Entre com o número a ser fatoriado: "))
    fatorial = 1
    i = 0
    while num-i > 0:
        fatorial = fatorial*(num-i)
        i += 1
    return fatorial

n = 1
while n >= 0:
    n = int(input("Entre: "))
    print(fatorial(n))
