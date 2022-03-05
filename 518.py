"""
A = [1, 2, 3]
B = [2, 5, 7, 6] +
    -------------
C = [3, 7, 10, 6]
"""

from random import randint


def preencheVetor(tam, a, b, aleatorio=True):
    v = []
    n = 1
    while n <= tam:
        if aleatorio:
            valor = randint(a, b)
            v.append(valor)
        else:
            print(f"Introduza o valor {n} de {tam} (entre {a} e {b}): ")
            valor = int(input())
            if valor >= a and valor <= b:
                v.append(valor)
            else:
                print(f"AVISO: Tem de inserir numeros entre {a} e {b}.")
        n += 1
    return v


def main():
    print()
    a = preencheVetor(10, 1, 100, aleatorio=True)
    b = preencheVetor(6, 1, 100, aleatorio=True)
    c = []

    print(a)
    print(b)

    tam = max(len(a), len(b))
    for x in range(tam):
        soma = 0

        if x < len(a):
            soma += a[x]
        if x < len(b):
            soma += b[x]

        c.append(soma)

    print(c)


# inicio do programa
main()
