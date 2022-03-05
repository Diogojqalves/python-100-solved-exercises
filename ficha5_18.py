'''
Crie um programa para somar 2 vetores de tamanhos diferentes 
e colocar o resultado num 3º vetor.
'''

a = [1, 2, 3]
b = [5, 7]
soma = 0
total = 0
for x in range(len(a)):
    soma = a[x] + soma

for x in range(len(b)):
    total = b[x] + soma

novo = soma + total

vetor = [novo]
print(vetor)
