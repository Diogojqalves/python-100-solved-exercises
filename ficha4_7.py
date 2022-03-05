'''
Crie uma função que receba dois valores inteiros como argumentos 
e retorne um valor booleano indicando se os números são divisíveis
'''
num = int(input('Introduza um número: '))
n = int(input('Introduza um número: '))

def divisiveis(a, b):
    if a % b == 0:
        return True
    else:
        return False

divisiveis(num, n)
print(divisiveis(num, n))

