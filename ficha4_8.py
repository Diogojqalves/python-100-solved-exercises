'''
Crie uma função que receba um número inteiro como argumento e 
retorne o número da série de Fibonacci correspondente.
'''
teclado = int(input('Introduza um nr inteiro: '))

def inteiro(num):
    a, b = 0, 1
    fib = a + b
    if num == 0:
        return 0
    else:
        while num > 1: # 0 e 1 são as primeiras du
            a = b
            b = fib
            fib = a + b
            num -=1
        return fib

print(inteiro(teclado))