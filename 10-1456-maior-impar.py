total = 1
maiorImpar = -9999
posmaiorImpar = -1
while True:
    n = int(input('introduza no numero' + str(total) + ':'))
    if n != '':
        n = int(n)
        if n == 0:
            break

        if n % 2 != 0:
            if n > maiorImpar:
                maiorImpar = n
                posmaiorImpar = total
        total += 1
    else:
        print('tem de introduzir um número inteiro')

if total == 1:
    print('Não foi inserido qualquer número válido')
else:
    if maiorImpar == -9999:
        print('Não foi inserido qualquer número impar')
    else:
        print(f'o maior numero impar é o {maiorImpar}, e foi introduzido na posição {posmaiorImpar}')