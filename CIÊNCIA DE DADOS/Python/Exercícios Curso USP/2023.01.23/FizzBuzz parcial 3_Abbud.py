VarA=int(input("Entre com o número a ser avaliado: "))

div3=VarA%3
div5=VarA%5

if div3==0 and div5==0:
    print("FizzBuzz")
else:
    print(VarA)
