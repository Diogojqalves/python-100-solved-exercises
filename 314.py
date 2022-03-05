"""
Escreva um programa que apresente todos os números inteiros 
entre dois números float introduzidos pelo utilizador
"""

a = float(input('escreva o 1o nr: '))
b = float(input('escreva o 2o nr: '))

c = int(a)
d = int(b)

for x in range (c, d +1):
    print(x)