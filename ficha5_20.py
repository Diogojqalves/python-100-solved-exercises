'''
 Crie um programa que simule 100 lançamentos de 2 dados, guarde 
os resultados em vetores e produza uma estatística
'''

import random

vetor = []
total = 0
p = 100
while p > 1:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    vetor.append(a)
    vetor.append(b)
    total = total + a + b
    p -= 1

media = total // 200
print(vetor)
# print('média de lançamento dum dado = %.2f' % media)
print(f'média de lançamento dum dado = {media}')
