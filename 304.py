# Crie um programa que escreva os números inteiros entre 0 e 100
# em intervalos (incremento) dados pelo utilizador. O intervalo
# deverá ser um número entre 1 e 10. (Por exemplo, com intervalos
# de 4).

inc = 0
 
while inc < 1 or inc > 10:
    consola = input('digite o valor de incremente entre 1 e 10: ')
    if consola.isdigit():
        inc = int(consola)
        if inc >= 1 and inc <= 10:
            for x in range(0, 101, inc):
                print(x, end=" ")
        else:
            print('o nr deverá estar entre 1 e 10')
    else:
        print(f'{consola}, não é um número')
