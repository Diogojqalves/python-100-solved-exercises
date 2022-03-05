'''
Escreva um programa que peça as idades de 32 alunos de uma 
turma. O programa deve guardar estes valores num vetor e no final 
indicar a idade máxima, mínima média e moda da turma.

'''

vetor = []
y = 0
m = 20
alunos = 6

while len(vetor) < alunos:
    n = int(input('Introduza a nota: '))
    vetor.append(n)
    if n > y:
        y = n
    if n < m:
        m = n
print(f'{y} é o valor máximo')
print(f'{m} é o valor minimo')

total= 0
mediana = -1
for x in vetor:
    total = total + x
    if vetor.count(x) > mediana:
        mediana = vetor[x]

media = total / alunos
print('%.2f é a média' % media)
print(f'{mediana} é a mediana')

