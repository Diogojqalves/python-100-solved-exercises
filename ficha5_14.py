'''
Escreva um programa que verifique se todos os elementos de um 
determinado vetor existem noutro vetor
'''


vetor = [1, 2, 3, 4]
determinado = [3, 4, 5, 6]
existe = True
for i in range(len(vetor) - 1):
    if determinado.count(vetor[i]) < 1:
        existe = False
   


if existe == True:
    print('todos os elementos de um determinado vetor existem noutro vetor')
else:
    print('todos os elementos de um determinado vetor não existem noutro vetor')
