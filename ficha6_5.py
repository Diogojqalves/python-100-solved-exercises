'''
 Crie um programa que leia 2 strings do utilizador e indique qual das strings está 
primeiro na ordem alfabética
'''

teclado = str(input('Escreva uma palavra: '))
palavra = str(input('Escreva uma palavra: '))

if teclado < palavra:
    print(teclado)
    print(palavra)
else:
    print(palavra)
    print(teclado)
