'''
Altere o programa para produzir o seguinte efeito:
g
ng
ing
ring
tring
string
'''

palavra = str(input('Escreva uma palavra: '))
palavra = palavra.strip()
imprime = ''
tamanho = len(palavra)
inverso = tamanho // -1

for x in range(-1, inverso, -1):
    imprime = imprime + palavra[x]
    print(imprime)

print(palavra.lower())