"""
Aproveite o programa anterior para escrever um programa que 
realize a soma, subtração, multiplicação e divisão de frações e 
apresente o resultado na forma reduzida.
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

"""Questionar prof, ex demasiado longo --- desconhecimento regras de frações"""