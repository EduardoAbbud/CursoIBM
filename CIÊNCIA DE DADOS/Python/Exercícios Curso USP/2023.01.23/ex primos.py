num = int(input("Número: "))
i = 2
primo = True
while i < num and primo:
    resto = num % i
    i += 1
    if resto == 0:
        primo = False

if primo:
    print("primo")
else:
    print("não primo")
