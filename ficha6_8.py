'''
Crie um programa que, numa string substitua todas as letras “v” por “b” e todas 
as ocorrências de “ão” por “om”
'''

palavra = 'Viva'
frase = 'Pão, cão, fão'

palavra = palavra.replace('v', 'b')
palavra = palavra.replace('V', 'b')
frase = frase.replace('ão', 'om')

print(palavra)
print(frase)


