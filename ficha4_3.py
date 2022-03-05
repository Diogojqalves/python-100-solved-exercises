'''
Crie uma função que receba dois valores float como argumentos e 
retorne o valor da raiz quadrada da soma dos quadrados
'''
import math

def funcao(prim, seg):
    quad = prim * prim
    quad2 = seg * seg
    soma = quad + quad2
    raiz = math.sqrt(soma)
    print(str(raiz))

n = float(input('introduza o 1valor: '))
nu = float(input('introduza o 2valor: '))
funcao(n, nu)