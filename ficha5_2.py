"""
Escreva um programa que procure e indique o maior valor (e a 
respetiva posição) de um vetor de 10 posições introduzido pelo 
utilizador.
"""

vetor = []
maior = -99999999

while len(vetor) < 10:
    i = int(input('Introduza um nr inteiro: '))
    vetor.append(i)
    if i > maior:
        maior = i

posicao = vetor.index(maior)
print(f'Maior valor inserido: {maior}, na posição {posicao}')