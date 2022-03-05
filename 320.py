"""
Escreva um programa em que o utilizador introduza números até 
introduzir um número par seguido de um número ímpar.
"""

while True:
    a = int(input('introduza um nr inteiro positivo: '))
    b = int(input('introduza um nr inteiro positivo: '))
    if (a % 2 == 0) and (b % 2 != 0):
        print('introduziu um número par seguido de um número ímpar, end game')
        break
