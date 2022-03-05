"""
Crie um programa que leia um vetor de n inteiros, sendo n um
valor introduzido pelo utilizador, não havendo restrições. O
programa deverá converter todos os valores negativos do vetor para
0, imprimir o vetor resultante e indicar quantos valores foram
alterados.
"""

vetor = []
n = int(input('Introduza N: ')) 
alt = 0

while n > 0:
    num = int(input('Introduza um valor inteiro: '))
    if num < 0:
        num = 0
        alt += 1
        vetor.append(num)
        n -= 1
    if num > 0:
        vetor.append(num)
        n -= 1

print(vetor)
print(f'{alt} nr/nrs foram alterados para 0')
