"""
Escreva um programa que leia n números 
(sendo n introduzido pelo utilizador) e indique se os números são 
todos iguais
"""

n = int(input('Quantos nrs pretende introduzir? '))
count = 0
flag = True

while count <= n:
    num = int(input('introduza o nr pretendido:'))
    count += 1
    if count == 1:
        a = num
    if count > 1:
        b = num
        while a == b:
            flag = True
        else:
            flag = False
else:
    print('')


if flag == True:
    print('todos os nr são iguais')
if flag == False:
    print('os nr n sao todos iguais ')