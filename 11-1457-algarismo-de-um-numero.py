num = 0 

while num <=0:
    num = int(input('digite um numero inteiro positivo'))
    if not num > 0:
        print('deve introduzir num numero maior do que zero')

output = ''
while num > 0:
    alg = num % 10
    output = str(alg) + '' + output
    num = num // 10

print(output)