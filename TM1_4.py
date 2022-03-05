"""
Um número de n dígitos é um número de Armstrong se é igual à soma de cada um dos seus dígitos 
elevado a n-ésima potência. Ex: 153 (n = 3 dígitos) é igual a 1^3 + 5^3 + 3^3.
a. Escreva um algoritmo capaz de determinar se um número natural dado é ou não um número de 
Armstrong.
"""
num = int(input('introduza um nr: '))
digitos = num
digito = num
count = 0
arm = 0

#descobrir quantos algarismos tem um número
while digitos > 0:
    digitos = digitos // 10
    count += 1

print(f"{num} tem {count} algarismos") # count = potência

# calcular o valor de cada algarismo elevado à potência e somar o valor total
while digito > 0:
    alg = digito % 10
    pot = alg**count
    arm += pot
    digito = digito // 10
    
    
if arm == num:
    print(f"{arm} = soma das potencias")
    print(f'{num} é um nr armstrong')
if arm != num:
    print(f"{arm} = soma das potencias")
    print(f'{num} n é um nr armstrong')


"""
b. Escreva um algoritmo que imprima os números de Armstrong entre um intervalo dado pelo 
utilizador. 
"""

a = int(input('introduza o 1º intervalo: '))
b = int(input('introduza o 2º intervalo: '))

for x in range(a, b +1):
    digitos = x
    digito = x
    count = 0
    arm = 0
    while digitos > 0:
        digitos = digitos // 10
        count += 1
    while digito > 0:
        alg = digito % 10
        pot = alg**count
        arm += pot
        digito = digito // 10
    if arm == x:
        print(f'{x} é um nr armstrong')