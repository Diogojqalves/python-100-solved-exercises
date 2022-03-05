'''
Crie um programa que leia 10 nomes para um vector de strings e os ordene 
alfabeticamente na saída
'''

vetor = []
n = 0
while n < 5:
    teclado = str(input('Introduza um nome: '))
    vetor.append(teclado)
    n += 1


vetor.sort()
print(vetor)