# Crie um programa que determine se um número inteiro é primo

num = int(input('Introduza um número inteiro:'))

if (num % 2 != 0) or (num == 2):
    print(f"{num} é um nr primo")
else:
    print(f"{num} n é um nr primo")