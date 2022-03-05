"""
Escreva um programa que apresente a tabuada dum número inteiro
entre 1 e 9 dado pelo utilizador. Se o número estiver fora dessa
gama, o programa deverá dar uma mensagem.
"""
contador = 1
a = int(input('Introduza um nr inteiro entre 1 e 9: '))
while contador < 11:
    if a > 0 and a < 10:
        p = a * contador
        print(f'{p}')
        contador += 1
    else:
        print('nr inválido')
        break

