'''
Crie um programa que leia um nome de um utilizador e apresente apenas o 
primeiro e o último nome. 
'''

nome = str(input('Escreva o seu nome completo: '))
nome = nome.strip()
print(nome)

alcunha = nome.split()
print(alcunha[0] + ' ' + alcunha[-1])