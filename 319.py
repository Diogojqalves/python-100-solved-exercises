"""
Escreva um programa que leia 10 números do utilizador e 
indique, no fim, quantos números são primos, quantos são pares e 
quantos são divisíveis por 3
"""

nums = 10

par = 0
primo = 0
div = 0

while nums > 0:
    num = int(input('Introduza um nr: '))
    nums -= 1
    a = num
    if (a % 2 != 0) or (a == 2):
        primo += 1
    if (a % 3 == 0):
        div += 1
    if (a % 2 == 0):
        par += 1

print(f'{par} nrs são par')
print(f'{primo} nrs sao primos')
print(f'{div} sao divisiveis por 3')