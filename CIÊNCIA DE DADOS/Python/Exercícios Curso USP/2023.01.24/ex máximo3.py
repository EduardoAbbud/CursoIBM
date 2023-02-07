def maximo(a,b,c):
    if a > b and a > c:
        max = a
    else:
        if b > c:
            max = b
        else:
            max = c
    return max
