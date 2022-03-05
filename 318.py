"""
Escreva um programa em que o utilizador vai introduzindo 
números inteiros positivos até o número introduzido ser um número 
primo
"""

while True:
    a = int(input('introduza um nr inteiro positivo: '))
    if a > 0:
        b = a
        if (b % 2 != 0 ) or (b == 2):
            print(f'{b} é um nr primo, end game :)')
            break
    else:
        print('Aviso: nr inválido')