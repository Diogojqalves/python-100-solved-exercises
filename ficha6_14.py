
'''
Escreva um programa para determinar quantas vezes uma substring existe numa 
string.
'''

word = str(input('introduza uma string: '))
subword = str(input('escolha uma palavra da string anterior: '))
word = word.strip()
subword = subword.strip()
palavra = word.lower()
subpalavra = subword.lower()

print(palavra.count(subpalavra))

