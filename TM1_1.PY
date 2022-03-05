"""
Codifique um programa que receba vários números inteiros positivos e imprima o produto dos números 
ímpares digitados e a soma dos números pares digitados. O programa deverá encerrar quando o zero 
ou um número negativo for digitado.
"""

impar = 0
par = 0
while True:
    num = int(input('introduza um nr: '))
    if num < 1:
        break
    if num % 2 == 0:
        par = num + par
    if num % 2 != 0:
        impar = num + impar

print(f'soma dos pares = {par}')
print(f'soma dos impares = {impar}')