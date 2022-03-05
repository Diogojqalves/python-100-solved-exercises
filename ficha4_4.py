'''
Crie uma função que receba um número inteiro como argumento e 
retorne o maior valor primo inferior a esse argumento. Se o 
argumento for negativo, a função deverá retornar o valor zero
'''

argumento = int(input('numero: '))
def funcao (num):
    n = 2
    if num < 0:
        return 0
    elif num <= 3 and num >= 0:
        return n
    else:
        while n < num -1:
            n += 1
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                maior = n
        return maior

funcao(argumento)
print(funcao(argumento))