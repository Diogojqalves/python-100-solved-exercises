'''
Crie uma função que receba um número inteiro e retorne a soma 
dos seus algarismos.
'''

def soma(num):
    algarismo = 0
    total = 0
    if num < 10:
        return num
    else:
        while num >= 1:
            algarismo = num % 10
            total = total + algarismo
            num = num // 10
        return total


teclado = int(input('Introduza um número inteiro: '))
print(soma(teclado))