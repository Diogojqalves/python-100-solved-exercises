'''
Crie uma função que receba 2 valores inteiros como argumentos e 
retorne a sua soma. Se o valor da soma for negativo a função deverá 
retornar o valor 0
'''

def funcao(a, b):
    if a + b < 0:
        print('0')
    else:
        print(a+b)


valor = int(input('Introduza o primeiro valor inteiro: '))
n = int(input('Introduza o segundo valor inteiro: '))
funcao(valor, n)