'''
Crie um programa que conte o número de números primos num 
vetor de inteiros
'''

vetor = [3, 5, 20, 29, 35]
contador = 0


for num in vetor:
    for x in range(2, num):
        if num % x == 0:
            break
    else:
        contador += 1


print(vetor)
print(contador)