'''
Crie um programa que leia um vetor de 10 inteiros. Os valores
deverão estar no intervalo [0,100]. O programa não deverá aceitar
valores fora deste intervalo. O programa deverá indicar a soma dos
inteiros múltiplos de 5 existentes no vetor.
'''

vetor = []
count = 0
soma = 0

while count < 10:
    num = int(input('introduza um nr entre 0 e 100: '))
    if num < 0 or num > 100:
        print('escolha um nr diferente')
    else:
        vetor.append(num)
        count += 1
        for x in range(1, 21):
            multiplos = 5 * x
            if num == multiplos:
                soma = multiplos + soma
                

print(vetor)
print(soma)