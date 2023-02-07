decrescente = True
anterior = int(input("Digite primeiro número da sequência: "))
valor = 1
while valor != 0 and decrescente == True:
    valor = int(input("Digite próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("Sequência está na ordem decrescente.")
else:
    print("Sequência não está na ordem decrescente.")
