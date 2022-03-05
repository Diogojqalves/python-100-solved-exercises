"""
Escreva um programa que peça ao utilizador um nome e um número
inteiro (entre 1 e 20). Deverá mostrar esse nome um número de
vezes igual a esse valor inteiro.
"""

nome = str(input('introduza um nome:'))
nr = int(input('introduza um nr inteiro entre 1 e 20: '))
ciclo = 1

while ciclo <= nr:
    print(nome)
    ciclo += 1
