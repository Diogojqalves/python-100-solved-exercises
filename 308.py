"""
Escreva um programa em que o utilizador vai introduzindo as
idades dos alunos de uma determinada turma até ser introduzido o
número -1. No fim deverá indicar o número de alunos e a média de
idades. O programa deverá garantir que apenas são introduzidos
números positivos (com a exceção do -1 final).
"""

totalIdades = 0
somaIdades = 0.0

while True:
    entrada = input('Introduza idades:')

    if entrada == '-1':
        break

    if entrada.isdigit():
        idade = int(entrada)
        if idade > 3 and idade <=130:
            totalIdades += 1
            somaIdades += idade
        else:
            print('aviso: idade inválida')
    else:
        print('aviso: só são permitidos valores numéricos')


# calcular a média
if totalIdades > 0:
    mediaIdades = somaIdades / totalIdades
    print(f'nº de alunos: {totalIdades}')
    print('media de idades: %.2f anos' % mediaIdades)
else:
    print('Aviso idade inválida')