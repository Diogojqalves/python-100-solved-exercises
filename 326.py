"""
 Escreva um programa que reduza uma fração
"""

numerador = int(input('insira o numerador: '))
denominador = int(input('insira o denominador: '))

i = 2
while i < (numerador and denominador) + 1:
        if numerador % i == 0 and denominador % i == 0:
            numerador = numerador // i
            denominador = denominador // i
        else:
            i += 1

print(numerador, denominador)
