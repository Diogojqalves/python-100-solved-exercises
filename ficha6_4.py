'''
 Crie um programa que “limpe” os espaços iniciais e finais de uma string.
'''


teclado = str(input('escreva uma frase: '))
vetor = list(teclado)

print(vetor)

while vetor[0] == ' ':
    vetor.pop(0)
while vetor[-1] == ' ':
    vetor.pop(-1)

print(vetor)
frase = ''.join(vetor)
print(frase)