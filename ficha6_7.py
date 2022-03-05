'''
 Crie um programa que inverta uma string.
'''

frase = str(input('escreva uma palavra: '))

reverse = frase[::-1]

print(reverse)

reverter = list(frase)
reverter.reverse()
composta = ''.join(reverter)
print(composta)