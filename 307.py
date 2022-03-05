i = 1
minimo = 999
maximo = -999
soma = 0.0
while i <= 10:
    consola = input(f'Digite o numero {i}: ')
    if consola.isdigit():
        num = int(consola)
        if num > 0:
            i += 1
            soma += num
            if num > maximo:
                maximo = num
            else:
                if num < minimo:
                    minimo = num
        else:
            print('o nr deverá ser maior do que zero')
    else:
        print(f'{consola} não é um nr.')


#imprimir
media = soma / 10
print('Resultados:')
print('\tSoma:', soma)
print('\tMedia: %.2f' % media)
print('\tMinimo:', minimo)
print('\tMaximo:', maximo)