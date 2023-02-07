num = int(input("Digite o valor de n: "))

tamanho=len(str(num))
i = 0
somaDg = 0

while i < tamanho:
    dig=num // (10 ** i) % 10
    somaDg += dig
    i += 1

print(somaDg)
