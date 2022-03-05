"""
Escreva um programa que preencha um vetor de 100 posições com os
primeiros 100 números pares.
"""

vetor = []

for x in range(1, 1000):
    if (len(vetor) < 100) and (x % 2) == 0:
            vetor.append(x)

print(vetor)
