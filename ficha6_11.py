'''
Crie um programa de modo a que uma string seja impressa do seguinte modo:
S
St
Str
Stri
Strin
string
'''

palavra = str(input('Escreva uma palavra: '))
palavra = palavra.strip()
palavra = palavra.capitalize()
imprime = ''


for x in range(0, len(palavra) - 1):
    imprime = imprime + palavra[x]
    print(imprime)

print(palavra.lower())