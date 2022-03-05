'''
Desenvolva um programa para simular o embaralhar de um baralho 
de cartas. Use um vetor e embaralhe as cartas fazendo trocas entre 
os elementos. Depois dê 4 mãos de 13 cartas
'''
import random

cores = ['copas', 'espadas', 'ouro', 'paus']
numero = ['As', 'J', 'K', 'D', '7', '6', '5', '4', '3', '2']

maos = 0
mao = 0
vetor = []
segunda = []
terceira = []
quarta = []

while len(vetor) < 13:
    carta = random.choice(cores)
    figura =random.choice(numero)
    vetor.append(figura + ' de ' + carta)
    mao += 1

while len(segunda) < 13:
    carta = random.choice(cores)
    figura =random.choice(numero)
    segunda.append(figura + ' de ' + carta)
    mao += 1

while len(terceira) < 13:
    carta = random.choice(cores)
    figura =random.choice(numero)
    terceira.append(figura + ' de ' + carta)
    mao += 1

while len(quarta) < 13:
    carta = random.choice(cores)
    figura =random.choice(numero)
    quarta.append(figura + ' de ' + carta)
    mao += 1

print(vetor)
print(segunda)
print(terceira)
print(quarta)