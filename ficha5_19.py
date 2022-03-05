'''
Crie um programa para determinar o maior valor entre as 
posições de dois vetores e colocar o resultado num 3º vetor
'''

vetor = [1, 5, 10]
compara = [7, 8, 9]
total = []

for x in range(0, len(vetor)):
    if vetor[x] > compara[x]:
        total.append(vetor[x])
    else: 
        total.append(compara[x])

print(total)
