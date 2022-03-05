'''
Crie uma função contaPrimos() que receba dois valores inteiros como argumentos e retorne o número de números primos entre estes dois números, inclusive. 
P. Ex. contaPrimos(3,10) deverá retornar o valor 3 (3, 5, 7). 
A função deverá ser testada sendo que os dois valores são introduzidos pelo utilizador.
'''
arg = int(input('Introduza o primeiro valor inteiro: '))
par = int(input('Introduza o segundo valor inteiro: '))

def contaPrimos(n, num):
    for i in range(n, num + 1):
        for x in range(2, i):
            if i % x == 0:
                 break
        else:
                 print(i) 
             # return maior

contaPrimos(arg, par)