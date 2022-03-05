'''
Crie uma função que verifique se um número é primo (deverá 
retornar um valor booleano)
'''


def ePrimo(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

print(ePrimo(11))

