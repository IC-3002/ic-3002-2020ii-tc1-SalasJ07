from math import factorial

def e_cuadratica(n):
    e = 0
    for i in range(0, n):
        e += 1/factorial(i)
    return(e)


def e_lineal(n):
    e = 0
    f = 1
    for i in range(1, n):
        e += 1/f
        f *= i
    return(e)
