"""
Escreva um programa que leia 10 números inteiros e indique se 
um número é igual ao anterior. No final deverá indicar quantos 
números introduzidos são iguais ao anterior.
"""
p = 10

while p > 0:
    if p == 10:
        a = int(input('introduza o 1º nr: '))
        if a > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')

    if p == 9:
        b = int(input('introduza o 2º: '))
        if b > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 8:
        c = int(input('introduza o 3º : '))
        if c > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 7:
        d = int(input('introduza o 4º : '))
        if d > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 6:
        e = int(input('introduza o 5º : '))
        if e > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 5:
        f = int(input('introduza o 6º: '))
        if f > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 4:
        g = int(input('introduza o 7º: '))
        if g > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 3:
        h = int(input('introduza o 8º: '))
        if h > 0 :
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 2:
        i = int(input('introduza o 9.º: '))
        if i > 0 :
            p = p - 1
        else:
            print('o nr tem de ser maior que zero')
    if p == 1:
        j = int(input('introduza o 10ª: '))
        if j > 0:
            p = p - 1
        else:
            print('o nr tem de ser maior do que zero')

iguais = 0
if a == b:
    iguais += 1
if b == c:
    iguais += 1
if c == d:
    iguais += 1
if d == e:
    iguais += 1
if e == f:
    iguais += 1
if f == g:
    iguais += 1
if g == h:
    iguais += 1
if h == i:
    iguais += 1
if i == j:
    iguais += 1

print(f'{iguais} números são iguais ao anterior')