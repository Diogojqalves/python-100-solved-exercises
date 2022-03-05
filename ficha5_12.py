'''
Escreva um programa que indique se todos os valores de um 
vetor são iguais, se são todos diferentes, ou se há valores 
repetidos no vetor. Para testar utilize um vetor cujo tamanho e 
valores inteiros são introduzidos pelo utilizador.
'''

vetor = []
tamanho = int(input('Introduza o tamanho do vetor: '))
contador = 0

while contador < tamanho:
    teclado = int(input('Introduza um valor: '))
    vetor.append(teclado)
    contador += 1

iguais = False
if vetor.count(teclado) == tamanho:
    iguais =  True
    print('Todos os números são iguais')

diferentes = False
repetidos = False
for x in vetor:
    if vetor.count(x) > 1:
        diferentes = True
    if vetor.count(x) > 1 and diferentes == True and iguais == False:
        repetidos = True
        
if diferentes == False:
    print('Os números são todos diferentes')
if repetidos == True:
    print('Há valores repetidos')

print(vetor)

