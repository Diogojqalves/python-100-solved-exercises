'''
Crie uma função que receba 3 valores float como argumento e 
retorne o maior valor absoluto
'''

def funcao(prim, seg, ter):
    if prim > seg and prim > ter:
        print(str(prim) + ' é o maior valor absoluto')
    elif seg > prim and seg > ter:
        print(str(seg) + ' é o maior valor absoluto')
    else:
        print(str(ter) + ' é o maior valor absoluto')

n = float(input('introduza o 1valor: '))
nu = float(input('introduza o 2valor: '))
num = float(input('introduza o 3valor: '))
funcao(n, nu, num)