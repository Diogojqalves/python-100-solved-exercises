'''
Crie um programa que apresente a soma de todos os valores de um
vetor de inteiros de 10 posições. Os valores devem ser introduzidos
pelo utilizador.
'''

vetor = []
n = 0 

while n < 10:
    num = int(input('Introduza um valor inteiro positivo: '))
    if num > 0 :
        vetor.append(num)
        n += 1
    else:
        print('Não pode inserir nrs inferiores a 1')

soma = 0
for i in vetor:
    soma = i + soma

print(soma)
print(vetor)