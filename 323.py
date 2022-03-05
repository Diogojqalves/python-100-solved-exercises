'''
Escreva um programa que indique ao utilizador todos os números 
primos entre dois números inteiros introduzidos pelo utilizador
'''

while True:
    a = int(input('1.º nr inteiro: '))
    if a > 0:
        b = int(input('2.º nr inteiro: '))
        if b > 0:
            break

for x in range(a, b + 1):
    if (x % 2 != 0) or (x ==2):
        print(x)