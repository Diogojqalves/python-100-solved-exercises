'''
Escreva um programa para determinar o valor mais comum (moda) 
num vetor de inteiros. Teste com um vetor de 100 posições preenchido 
aleatoriamente com valores entre 0 e 10
'''
import random
vetor = []
p = 100
while p > 1:
    n = random.randint(0, 10)
    vetor.append(n)
    p -= 1

x = -1
for i in range(0, 11):
    if vetor.count(i) > x :
        moda = i
        x = vetor.count(i)

for y in range(0, 11):
    if vetor.count(moda) == vetor.count(y):
        print(y)
    


