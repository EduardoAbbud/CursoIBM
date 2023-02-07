def maior_primo(numM):
    i = numM
    primoV = True
    while i > 0 and primoV:
        a = primo(i)
        if a != "não primo":
            return i
            primoV = False
        i = i - 1
       
def primo(num):
    i = 2
    primo = True
    while i < num and primo:
        resto = num % i
        i += 1
        if resto == 0:
            primo = False

    if primo:
        return "primo"
    else:
        return "não primo"


