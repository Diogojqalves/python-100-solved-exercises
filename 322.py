VINTE = 20 # caps = const, var no qual o valor n altera
while True:
    num = int(input('introduza um nr inteiro: '))
    if num > 0:
        somaAlg = 0
        while num > 0:
            somaAlg += (num % 10)
            num //= 10
        if somaAlg > VINTE:
            print('a soma dos algarismos é superior a 20')
            break

    else:
        print('tem de inserir um nr inteiro positivo')