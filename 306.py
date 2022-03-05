'''
Crie um programa para escrever a série de quadrados entre 1 e 
um valor inteiro inferior a 100 introduzido pelo utilizador. (1, 
4, 9, 25...)
'''

while True:
    a = int(input(' introduza um nr interior inferior a 100: '))
    if (a < 101) and (a > 0):
        break
    else:
        print('nr invalido')


for x in range(a, 101):
    print(x * x)

