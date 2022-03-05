#Escreva um programa para imprimir todos os números inteiros
#entre dois valores introduzidos pelo utilizador.
# O programa deverá verificar qual dos dois valores é o maior.

p = 2

while p > 0:
    if p == 2:
        a = int(input('introduza o 1º nr: '))
        if a > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')

    if p == 1:
        b = int(input('introduza o 2º limite: '))
        if b > 0 and b != a:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero e diferente do primeiro valor')

#determinar limite inferior e superior
minimo = a
maximo = b
if a > b:
    minimo = b
    maximo = a

#imprimir valor
for x in range(minimo, maximo + 1):
    print(x, end=" ")