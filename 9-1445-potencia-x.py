while True:
    base = int(input('introduza a base:'))
    expoente = int(input('introduza o expoente:'))

    if base > 0 and expoente > 0:
        break
    else:
        print('Por favor, introduza valores válidos')

potencia = 1
for x in range(1, expoente + 1): # +1 porque o expoente é exclusivo, não aceita o último valor da lista
    potencia *= base

print(f'{base}^{expoente} = {potencia}')