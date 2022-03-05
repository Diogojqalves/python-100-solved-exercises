'''
Crie um programa que leia um vetor de 10 valores inteiros do
utilizador, não permitindo a introdução de valores repetidos.
'''

vetor = []
n = 0 

while n < 10:
    num = int(input('Introduza um valor inteiro positivo: '))
    if num > 0 and vetor.count(num) == 0:
        vetor.append(num)
        n += 1
    else:
        print('Não pode inserir nrs repetidos ou inferiores a 0')
print('Fim de programa')