'''
Escreva um programa em que o utilizador vai introduzindo 
números positivos até ser introduzido o valor 0 (zero). No fim o 
programa indicará a percentagem de números pares introduzidos.
'''

total = 0
pares= 0

while True:
    a = int(input('introduza um nr positivo:'))
    if a > 0:
        total += 1
        if (a % 2 == 0):
            pares += 1
    if a == 0:
        total += 1
        break

media = (pares * 100) / total
print('percentagem arredonda de nr pares introduzidos = %d' % (media))