"""
Crie um programa que leia um conjunto de valores inteiros do
utilizador e os coloque num vetor. O programa deverá terminar a
leitura quando for introduzido um número que já exista no vetor, ou
seja, quando for introduzido um número repetido. No final deverá
apresentar o vetor.
"""

vetor = []
n = True 

while n == True:
    num = int(input('Introduza um valor inteiro positivo: '))
    if num > 0 and vetor.count(num) == 0:
        vetor.append(num)
    elif num > 0 and vetor.count(num) > 0:
        print(vetor)
        n = False
    else:
        print('Não pode inserir nrs repetidos ou inferiores a 0')

print('Fim de programa')