'''
 Crie uma função que receba 3 valores inteiros (a, b, c) e 
retorne um valor booleano true se a > b > c e false em caso 
contrário
'''

def tres(a, b, c):
    if a > b and b > c:
        return True
    else:
        return False

print(tres(5, 4, 3))