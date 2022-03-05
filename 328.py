"""
Escreva um programa que, a partir do preço em euros e do
dinheiro entregue, apresente o troco usando o menor número
possível de moedas.
"""

precoEuros, valorPago = 0.0, 0.0
perguntas = 2

# ler preço em euros e valor pago
while perguntas > 0:
    if perguntas == 2:
        precoEuros = float(input('introduza o preço em euros: '))
        if precoEuros > 0.0:
            perguntas -= 1
        else:
            print('Aviso preço tem de ser maior do que zero')
    if perguntas == 1:
        valorPago = float(input('introduza o preço em euros: '))
        if valorPago >= precoEuros:
            perguntas -= 1
        else:
            print('Aviso: valor entregue tem de ser superior ao preço')

# calcular troco
troco = round(valorPago - precoEuros, 2)

if troco == 0.0:
    print('entregou valor certo')
else:
    print(f'troco a receber: {troco}euros')
    t2, t1, t05, t02, t01, t005, t002, t001 = 0, 0, 0, 0, 0, 0, 0, 0
    while troco > 0.0:
        if troco >= 2.00:
            troco = round(troco - 2.00, 2)
            t2 += 1
        elif troco >= 1.00:
            troco = round(troco - 1.00, 2)
            t1 += 1
        elif troco >= 0.50:
            troco = round(troco - 0.50, 2)
            t05 += 1
        elif troco >= 0.20:
            troco = round(troco - 0.20, 2)
            t02 += 1
        elif troco >= 0.10:
            troco = round(troco - 0.10, 2)
            t01 += 1
        elif troco >= 0.05:
            troco = round(troco - 0.05, 2)
            t005 += 1
        elif troco >= 0.02:
            troco = round(troco - 0.02, 2)
            t002 += 1
        else:
            troco = round(troco - 0.01, 2)
            t001 += 1

# apresenta nr de moedas
if t2 > 0:
    print(f'{t2} moedas de 2euros')
if t1 > 0:
    print(f'{t1} moedas de 2euros')
if t05 > 0:
    print(f'{t05} moedas de 2euros')
if t02 > 0:
    print(f'{t02} moedas de 2euros')
if t01 > 0:
    print(f'{t01} moedas de 2euros')
if t005 > 0:
    print(f'{t005} moedas de 2euros')
if t002 > 0:
    print(f'{t002} moedas de 2euros')
if t001 > 0:
    print(f'{t001} moedas de 2euros')   



