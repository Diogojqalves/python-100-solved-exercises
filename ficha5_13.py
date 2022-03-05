'''
Crie um programa que leia um vetor de inteiros cujo tamanho 
será introduzido pelo utilizador, tamanho esse que nunca será 
inferior a 5 ou superior a 25. O programa deverá indicar ao 
utilizador se o vetor é constituído (ou não) por valores pares e 
ímpares alternados. Exemplo: O vetor [1, 2, 5, 6, 3, 2] verifica 
esta condição
'''

vetor = []
contador = 0

while True:
    tamanho = int(input('Escolha o tamanho do vetor, tamanho esse que nunca será inferior a 5 ou superior a 25: '))
    if tamanho > 4 and tamanho < 26:
        break
    else:
        print('tamanho não pode ser inferior a 5 ou superior a 25')

while contador < tamanho:
    teclado = int(input('Introduza um valor: '))
    vetor.append(teclado)
    contador += 1

print(vetor)
print(len(vetor))

alternado = False
for x in range(len(vetor)):
    if vetor[x] % 2 == vetor[x + 1] % 2:
        alternado = False
        break
    else:
        alternado = True

if alternado == True:
    print('o vetor é constituído por valores pares e ímpares alternados')

if alternado == False:
    print('o vetor não é constituído por valores pares e ímpares alternados')





